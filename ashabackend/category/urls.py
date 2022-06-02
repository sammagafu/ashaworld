from django.urls import path
from . import views

urlpatterns = [
    path("category/",views.CategoryListView.as_view()),
    path("category/<str:slug>/",views.CategoryDetailView.as_view())
]
