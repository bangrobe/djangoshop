from django.urls import path
from apps.cart import views
urlpatterns = [
    path('', views.cart_detail, name='cart'),
    path('success/', views.success, name='success')
]
