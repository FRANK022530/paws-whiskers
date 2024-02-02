
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('administrator/', views.index, name='index'),
    path('storefront', views.storefront, name='storefront'),
    path('add/', views.Addproduct, name='addproduct'),
    path('additem/', views.additem, name='additem'),
    path('addorder/<int:id>/', views.addorder, name='addorder'),
    path('administrator/delete/<int:id>', views.delete, name='delete'),
    path('received/<int:id>', views.received, name='received'),
    path('delivery/<int:id>', views.delivery, name='delivery'),
    path('cartdelete/<int:id>/', views.cartdelete, name='cartdelete'),
    path('administrator/update/<int:id>', views.update, name='update'),
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('register/', views.register, name='register'),
    path('', views.front, name='front'),
    path('login/', views.login, name='login'),
    path('UserRegister/', views.UserRegister, name='UserRegister'),
    path('LoginUser/', views.LoginUser, name='LoginUser'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('cart/', views.cart, name='cart'),
    path('Order/', views.Order, name='Order'),
    path('allorder/', views.allorder, name='allorder'),
    path('feedback/', views.feedback, name='feedback'),
    path('allfeedback/', views.allfeedback, name='allfeedback'),




]

