from django.urls import path

from .views import (
    index,
    login_view,
    register_view,
    DishTypeListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-types-list",
    ),
]

app_name = "kitchen"
