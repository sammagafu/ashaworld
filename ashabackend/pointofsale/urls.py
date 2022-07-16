from django.urls import path
from . views import PosclientViewSet,PosProductViewSet,PosOrderViewSet, PosProductQuantityViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register('',PosclientViewSet)

routerproduct = DefaultRouter()
routerproduct.register('',PosProductViewSet)
routerorder = DefaultRouter()
routerorder.register('',PosOrderViewSet)

routerquantity = DefaultRouter()
routerquantity.register('',PosProductQuantityViewSet)

urlpatterns = [
    path('client/',include(router.urls)),
    path('product/',include(routerproduct.urls)),
    path('order/',include(routerorder.urls)),
    path('product-quantity/',include(routerquantity.urls)),
]
