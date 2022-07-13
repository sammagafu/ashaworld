from rest_framework import viewsets
from . models import CompanyInformation,TeamMembers,Team
from .serializer import CompanyInformationSerializer,TeamSerializer,TeamMembersSerializer

class CompanyViewSet(viewsets.ModelViewSet):
     queryset = CompanyInformation.objects.all()
     serializer_class = CompanyInformationSerializer
     http_method_names = ['get','post','retrieve','put','patch']

class TeamViewSet(viewsets.ModelViewSet):
     queryset = Team.objects.all()
     serializer_class = TeamSerializer
     http_method_names = ['get','post','retrieve','put','patch']

class TeamMembersViewSet(viewsets.ModelViewSet):
     queryset = TeamMembers.objects.all()
     serializer_class = TeamMembersSerializer
     http_method_names = ['get','post','retrieve','put','patch']
