from django.urls import path
from . import views

urlpatterns = [
    path('',views.CartList.as_view()),
    path('add/',views.AddProductToCart.as_view())
]
