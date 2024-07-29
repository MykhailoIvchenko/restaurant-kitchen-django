from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.forms import RegistrationForm
from kitchen.models import Cook

COOKS_LIST_URL = reverse("kitchen:cooks-list")


class CreateCookFormTests(TestCase):
    def test_cook_creation_form_with_first_last_name_years_is_valid(self):
        form_data = {
            "username": "test_cook",
            "email": "test@gmail.com",
            "password1": "qwerty123test",
            "password2": "qwerty123test",
            "first_name": "Test",
            "last_name": "Cook",
            "years_of_experience": 5
        }

        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class SearchCookFormTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password",
            years_of_experience=3,
        )
        self.client.login(username="testuser", password="password")

        self.cook1 = Cook.objects.create(
            username="cook_one",
            years_of_experience=2
        )
        self.cook2 = Cook.objects.create(
            username="cook_two",
            years_of_experience=3
        )
        self.cook3 = Cook.objects.create(
            username="another_cook",
            years_of_experience=4
        )

    def test_search_no_query(self):
        response = self.client.get(COOKS_LIST_URL)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cook_one")
        self.assertContains(response, "cook_two")
        self.assertContains(response, "another_cook")

    def test_search_with_query(self):
        response = self.client.get(COOKS_LIST_URL, {"username": "one"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cook_one")

    def test_search_with_exact_match_query(self):
        response = self.client.get(COOKS_LIST_URL,
                                   {"username": "another_cook"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "another_cook")
        self.assertNotContains(response, "cook_one")
        self.assertNotContains(response, "cook_two")

    def test_search_with_no_results(self):
        response = self.client.get(COOKS_LIST_URL,
                                   {"username": "nonexistent"})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "cook_one")
        self.assertNotContains(response, "cook_two")
        self.assertNotContains(response, "another_cook")
