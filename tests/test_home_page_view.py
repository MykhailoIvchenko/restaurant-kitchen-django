from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Dish, DishType

HOME_PAGE_URL = reverse("kitchen:index")


class HomePageTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            years_of_experience=5,
            first_name="Admin",
            last_name="User",
            password="1qwerty2",
        )
        self.client.force_login(self.user)

    def test_index_count_content_correctly(self):
        response = self.client.get(reverse("kitchen:index"))
        num_cooks = get_user_model().objects.count()
        num_dishes = Dish.objects.count()
        num_dish_types = DishType.objects.count()

        self.assertContains(response, "Restaurant Kitchen")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/index.html")
        self.assertEqual(response.context["num_cooks"], num_cooks)
        self.assertEqual(response.context["num_dishes"], num_dishes)
        self.assertEqual(
            response.context["num_dish_types"],
            num_dish_types
        )
