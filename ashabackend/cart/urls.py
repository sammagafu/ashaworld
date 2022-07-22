from django.urls import path
from . import views

urlpatterns = [
    path('',views.CartList.as_view()),
    path('add/',views.AddProductToCart.as_view()),
    path('<int:owner>/delete',views.RemoveRetreiveUpdateDeleteCart.as_view()),
    path('wishlist/',views.AddProductToFavourite.as_view()),
    path('wishlist/<int:pk>/',views.RemoveRetreiveUpdateDeleteFavourite.as_view()),
]
