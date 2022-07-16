from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet,TeamViewSet,TeamMembersViewSet,get_my_team

router = DefaultRouter()
router.register('',CompanyViewSet)

routeruser = DefaultRouter()
routeruser.register('',TeamViewSet)

routerorder = DefaultRouter()
routerorder.register('',TeamMembersViewSet)

urlpatterns = [
    path('company-info/',include(router.urls)),
    path('team/',include(routeruser.urls)),
    path('team-member/',include(routerorder.urls)),
    path('my-team/', get_my_team, name='get_my_team'),
]
