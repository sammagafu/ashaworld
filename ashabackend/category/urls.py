from django.urls import path
from . import views
from product.views import GetProductsByCategory

urlpatterns = [
    path("<str:category_slug>/product/",GetProductsByCategory.as_view()),
    path("category/",views.CategoryListView.as_view()),
    path("category/<str:slug>/",views.CategoryDetailView.as_view())
]
