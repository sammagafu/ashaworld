from django.urls import path
from .views import ProductListview,ProductDetailView

app_name = "products"

urlpatterns = [
    path("",ProductListview.as_view()),
    path("<slug:category_slug>/<slug:product_slug>/",ProductDetailView.as_view(),name="details"),
]
