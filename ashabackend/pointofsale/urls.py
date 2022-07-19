from django.urls import path
from . views import PosclientViewSet,PosProductViewSet,PosOrderViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register('',PosclientViewSet)

routerproduct = DefaultRouter()
routerproduct.register('',PosProductViewSet)
routerorder = DefaultRouter()
routerorder.register('',PosOrderViewSet)



urlpatterns = [
    path('client/',include(router.urls)),
    path('product/',include(routerproduct.urls)),
    path('order/',include(routerorder.urls)),
]
