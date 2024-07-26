from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish

username = "test_user"
password = "test1234"
years_of_experience = 5


class ModelsTest(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Test dish type",
        )
        self.assertEqual(str(dish_type),
                         f"{dish_type.name}")

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name="Test",
            last_name="Cook",
            years_of_experience=years_of_experience
        )

        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})")

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Test Dish Type",
        )
        dish = Dish.objects.create(
            name="Test name",
            description="Test description",
            price=10,
            dish_type=dish_type
        )

        self.assertEqual(str(dish), dish.name)

    def test_create_cook_with_years_of_experience(self):
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password), password)
        self.assertEqual(cook.years_of_experience, years_of_experience)
