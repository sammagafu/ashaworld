from django.urls import path
from . views import PosclientViewSet,PosProductViewSet,PosOrderViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path,include

router = DefaultRouter()
router.register('',PosclientViewSet)

routeruser = DefaultRouter()
routeruser.register('',PosProductViewSet)

routerorder = DefaultRouter()
routerorder.register('',PosOrderViewSet)

urlpatterns = [
    path('client/',include(router.urls)),
    path('product/',include(routeruser.urls)),
    path('order/',include(routerorder.urls)),
]
