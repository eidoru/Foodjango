from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUp.as_view()),
    path("signin/", views.SignIn.as_view()),

    path("me/", views.Me.as_view()),

    path("restaurants/", views.RestaurantList.as_view()),
    path("restaurants/<int:restaurant_id>/", views.RestaurantDetail.as_view()),
    path("restaurants/<int:restaurant_id>/items/",
         views.RestaurantItemList.as_view()),
    path("restaurants/<int:restaurant_id>/items/<int:restaurant_item_id>/",
         views.RestaurantItemDetail.as_view()),

    path("carts/", views.CartList.as_view()),
    path("carts/<int:cart_id>/", views.CartDetail.as_view()),
    path("carts/<int:cart_id>/items/", views.CartItemList.as_view()),

    path("orders/", views.OrderList.as_view()),
    path("orders/<int:order_id>/", views.OrderDetail.as_view()),
    path("orders/<int:order_id>/items/", views.OrderItemList.as_view()),
]
