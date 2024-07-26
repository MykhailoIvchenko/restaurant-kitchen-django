from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish

DISHES_LIST_URL = reverse("kitchen:dishes-list")


class DishSearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password",
            years_of_experience=5,
        )
        self.client.login(username="testuser", password="password")

        self.dish_type1 = DishType.objects.create(name="TestOne")
        self.dish_type2 = DishType.objects.create(name="TestTwo")

        self.dish1 = Dish.objects.create(
            name="DishOne",
            description="Test Description",
            price="15",
            dish_type=self.dish_type1
        )
        self.dish2 = Dish.objects.create(
            name="DishTwo",
            description="Test Description",
            price="15",
            dish_type=self.dish_type2
        )
        self.dish3 = Dish.objects.create(
            name="DishThree",
            description="Test Description",
            price="15",
            dish_type=self.dish_type1
        )

    def test_search_no_query(self):
        response = self.client.get(DISHES_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DishOne")
        self.assertContains(response, "DishTwo")
        self.assertContains(response, "DishThree")

    def test_search_with_query(self):
        response = self.client.get(DISHES_LIST_URL, {"name": "one"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DishOne")
        self.assertNotContains(response, "DishTwo")
        self.assertNotContains(response, "DishThree")

    def test_search_with_partial_match_query(self):
        response = self.client.get(DISHES_LIST_URL, {"name": "ne"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DishOne")
        self.assertNotContains(response, "DishTwo")
        self.assertNotContains(response, "DishThree")

    def test_search_with_no_results(self):
        response = self.client.get(DISHES_LIST_URL, {"name": "nonexistent"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "DishOne")
        self.assertNotContains(response, "DishTwo")
        self.assertNotContains(response, "DishThree")
