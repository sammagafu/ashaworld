from django.urls import path
from . import views

urlpatterns = [
    path("",views.BrandListView.as_view()),
    path("<str:slug>/",views.BrandDetailView.as_view())
]
