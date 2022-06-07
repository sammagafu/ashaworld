from django.urls import path
from . import views

urlpatterns = [
    path("brand/",views.BrandListView.as_view()),
    path("brand/<str:slug>/",views.BrandDetailView.as_view())
]
