from . import views
from django.urls import path
urlpatterns = [
    path('',views.OrderListAPI.as_view()),
    path('<str:slug>/order',views.OrderItemRetrieveUpdateDeleteAPI.as_view()),
    path('orderitems/',views.OrderItemListAPI.as_view()),
    path('orderitems/<int:pk>',views.OrderItemRetrieveUpdateDeleteAPI.as_view()),

]
