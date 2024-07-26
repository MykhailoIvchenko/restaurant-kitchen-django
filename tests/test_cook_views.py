from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import Cook

COOKS_LIST_URL = reverse("kitchen:cooks-list")
PAGINATION = 5


class PublicCookTests(TestCase):
    def test_login_required(self):
        response = self.client.get(COOKS_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="admin.user",
            years_of_experience=3,
            first_name="Admin",
            last_name="User",
            password="1qwerty2",
        )
        self.client.force_login(self.user)

        for i in range(0, PAGINATION + 1):
            Cook.objects.create(
                username=f"cook.user{i}",
                years_of_experience=i,
                first_name=f"Admin{i}",
                last_name=f"User{i}",
                password=f"1qwerty{i}",
            )

    def test_cooks_list(self):
        response = self.client.get(COOKS_LIST_URL)
        cooks = Cook.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["cook_list"]),
            list(cooks[:PAGINATION]),
        )
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_cook_detail(self):
        response = self.client.get(reverse("kitchen:cook-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_detail.html")

    def test_cook_list_response_with_correct_template(self):
        response = self.client.get(COOKS_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_cook_detail_response_with_correct_template(self):
        response = self.client.get(reverse("kitchen:cook-detail", args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/cook_detail.html")

