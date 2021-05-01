from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('simulate/', views.simulate, name="simulate"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('login/', views.login, name="login")
]