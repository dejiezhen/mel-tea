from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
    path('update_item/', views.updateItem, name="update_item"), 
    path('chat/', views.room, name='chat'),
    path('guestChat/', views.guestChat, name='guestChat')
]