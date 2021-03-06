from rest_framework import viewsets
from rest_framework.response import Response
from . models import CompanyInformation,TeamMembers,Team
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .serializer import CompanyInformationSerializer,TeamSerializer,TeamMembersSerializer

class CompanyViewSet(viewsets.ModelViewSet):
     queryset = CompanyInformation.objects.all()
     serializer_class = CompanyInformationSerializer
     http_method_names = ['get','post','retrieve','put','patch']

    #  def list(self, request):
    #     queryset = CompanyInformation.objects.filter(owner=self.request.user)
    #     serializer = CompanyInformationSerializer(queryset, many=True)
    #     return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
     queryset = Team.objects.all()
     serializer_class = TeamSerializer
     http_method_names = ['get','post','retrieve','put','patch']

class TeamMembersViewSet(viewsets.ModelViewSet):
     queryset = TeamMembers.objects.all()
     serializer_class = TeamMembersSerializer
     http_method_names = ['get','post','retrieve','put','patch']


@api_view(['GET'])
def get_my_team(request):
     # print("request")
     member = Team.objects.filter(teammember__pk=request.user.id).get()
     company = CompanyInformation.objects.filter(team__pk=member.pk).get()
     print(CompanyInformationSerializer)
     serializer = CompanyInformationSerializer(company)
     return Response(serializer.data)