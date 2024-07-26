from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType

DISH_TYPES_LIST_URL = reverse("kitchen:dish-types-list")


class DishTypeSearchTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password",
            years_of_experience=3,
        )
        self.client.login(username="testuser", password="password")

        self.dish_type1 = DishType.objects.create(name="TestOne")
        self.dish_type2 = DishType.objects.create(name="TestTwo")
        self.dish_type3 = DishType.objects.create(name="TestThree")

    def test_search_no_query(self):
        response = self.client.get(DISH_TYPES_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestOne")
        self.assertContains(response, "TestTwo")
        self.assertContains(response, "TestThree")

    def test_search_with_query(self):
        response = self.client.get(DISH_TYPES_LIST_URL, {"name": "One"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestOne")
        self.assertNotContains(response, "TestTwo")
        self.assertNotContains(response, "TestThree")

    def test_search_with_partial_match_query(self):
        response = self.client.get(DISH_TYPES_LIST_URL, {"name": "ne"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestOne")
        self.assertNotContains(response, "TestTwo")
        self.assertNotContains(response, "TestThree")

    def test_search_with_no_results(self):
        response = self.client.get(DISH_TYPES_LIST_URL,
                                   {"name": "nonexistent"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "TestOne")
        self.assertNotContains(response, "TestTwo")
        self.assertNotContains(response, "TestThree")
