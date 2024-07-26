from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType

DISH_TYPES_LIST_URL = reverse("kitchen:dish-types-list")
PAGINATION = 5


class PublicDishTypeTests(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_TYPES_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            years_of_experience=5,
            first_name="Admin",
            last_name="User",
            password="1qwerty2",
        )
        self.client.force_login(self.user)

        for i in range(0, PAGINATION + 1):
            DishType.objects.create(
                name=f"Test Dish Type{i}",
            )

    def test_get_dish_types(self):
        response = self.client.get(DISH_TYPES_LIST_URL)
        self.assertEqual(response.status_code, 200)

    def test_dish_types_list(self):
        response = self.client.get(DISH_TYPES_LIST_URL)
        dish_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_types_list"]),
            list(dish_types[:PAGINATION]),
        )

    def test_dish_type_list_response_with_correct_template(self):
        response = self.client.get(DISH_TYPES_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_types_list.html")

    def test_dish_type_list_ordered_by_name(self):
        response = self.client.get(DISH_TYPES_LIST_URL)
        man_list = DishType.objects.all().order_by("name")
        dish_type_context = response.context["dish_types_list"]

        self.assertEqual(
            list(dish_type_context),
            list(man_list[: len(dish_type_context)]),
        )

    def test_create_dish_type(self):
        name = "Test Create"
        response = self.client.post(
            reverse(
                "kitchen:dish-type-create",
            ),
            {"name": name},
        )

        dish_type = DishType.objects.get(name=name)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(dish_type.name, name)

    def test_update_dish_type(self):
        name = "Test Update"
        updated_name = "Updated Name"

        dish_type = DishType.objects.create(
            name=name,
        )
        response = self.client.post(
            reverse(
                "kitchen:dish-type-update", kwargs={"pk": dish_type.id}
            ),
            {"name": updated_name},
        )
        DishType.objects.get(id=dish_type.id).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            DishType.objects.get(id=dish_type.id).name, updated_name
        )

    def test_delete_dish_type(self):
        dish_type = DishType.objects.create(
            name="Test Delete",
        )
        response = self.client.post(
            reverse("kitchen:dish-type-delete", kwargs={"pk": dish_type.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            DishType.objects.filter(id=dish_type.id).exists()
        )
