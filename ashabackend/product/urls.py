from django.urls import path
from .views import ProductListview,ProductDetailView

app_name = "products"

urlpatterns = [
    path("product/",ProductListview.as_view()),
    path("product/<slug:category_slug>/<slug:product_slug>/",ProductDetailView.as_view(),name="details"),
]
