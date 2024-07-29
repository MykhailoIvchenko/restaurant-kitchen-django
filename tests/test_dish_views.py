from django.test import TestCase

from django.contrib.auth import get_user_model
from django.urls import reverse

from kitchen.models import Dish, DishType

DISHES_LIST_URL = reverse("kitchen:dishes-list")
PAGINATION = 5

name = "Test Create"
description = "Test description"
price = 12
dish_type = "Test Dish Type"


class PublicDishTests(TestCase):
    def test_login_required(self):
        response = self.client.get(DISHES_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            years_of_experience=3,
            first_name="Admin",
            last_name="User",
            password="1qwerty2",
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(
            name=dish_type,
        )

        for i in range(0, PAGINATION + 1):
            Dish.objects.create(
                name=f"Test Name{i}",
                description=f"Test Description{i}",
                price=i + 1,
                dish_type=self.dish_type,
            )

    def test_dish_list(self):
        response = self.client.get(DISHES_LIST_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_list"]),
            list(dishes[:PAGINATION]),
        )
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_dish_detail(self):
        response = self.client.get(reverse("kitchen:dish-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_detail.html")

    def test_dish_list_response_with_correct_template(self):
        response = self.client.get(DISHES_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_dish_detail_response_with_correct_template(self):
        response = self.client.get(reverse("kitchen:dish-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_detail.html")

    def test_create_dish(self):
        response = self.client.post(
            reverse("kitchen:dish-create"),
            {
                "name": name,
                "description": description,
                "price": price,
                "dish_type": self.dish_type.id,
                "cooks": [self.user.id],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            Dish.objects.get(
                id=self.user.dishes.first().id).dish_type.name,
            dish_type
        )

    def test_update_dish(self):
        updated_name = "Updated Name"
        dish = Dish.objects.create(
            name=name,
            description=description,
            price=price,
            dish_type=self.dish_type,
        )
        response = self.client.post(
            reverse("kitchen:dish-update", kwargs={"pk": dish.id}),
            {
                "pk": dish.id,
                "description": description,
                "price": price,
                "name": updated_name,
                "dish_type": self.dish_type.id,
                "cooks": [self.user.id],
            },
        )
        Dish.objects.get(id=dish.id).refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dish.objects.get(id=dish.id).dish_type.name,
                         dish_type)

    def test_delete_dish(self):
        dish = Dish.objects.create(
            name=name,
            description=description,
            price=price,
            dish_type=self.dish_type,
        )
        response = self.client.post(
            reverse("kitchen:dish-delete", kwargs={"pk": dish.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=dish.id).exists())
