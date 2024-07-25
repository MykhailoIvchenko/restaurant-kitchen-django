from django.urls import path

from .views import (
    index,
    login_view,
    register_view,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
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
    path(
        "dish-types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish-types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish-types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
]

app_name = "kitchen"
