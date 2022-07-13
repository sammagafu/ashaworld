from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet,TeamViewSet,TeamMembersViewSet

router = DefaultRouter()
router.register('',CompanyViewSet)

routeruser = DefaultRouter()
routeruser.register('',TeamViewSet)

routerorder = DefaultRouter()
routerorder.register('',TeamMembersViewSet)

urlpatterns = [
    path('company-info/',include(router.urls)),
    path('team/',include(routeruser.urls)),
    path('team-members/',include(routerorder.urls)),
]
