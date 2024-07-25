from django.urls import path

from .views import (
    index,
    login_view,
    register_view,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CooksListView,
    CookDetailView, CookCreateView, CookUpdateView, CookDeleteView, DishListView,
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
    path(
        "cooks/",
        CooksListView.as_view(),
        name="cooks-list",
    ),
    path(
        "cook/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path(
        "cooks/create/", CookCreateView.as_view(), name="cook-create"
    ),
    path(
        "cooks/<int:pk>/update/", CookUpdateView.as_view(), name="cook-update"
    ),
    path(
        "cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dishes-list",
    ),
]

app_name = "kitchen"
