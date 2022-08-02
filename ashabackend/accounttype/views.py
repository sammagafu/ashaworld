from rest_framework import viewsets
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from . models import CompanyInformation,TeamMembers,Team
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework_csv import renderers as r
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .serializer import CompanyInformationSerializer,TeamSerializer,TeamMembersSerializer, UserSerializer


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

class TeamMemberListRenderer(r.CSVRenderer):
    header = ['member.id','member.email', 'member.address', 'member.phone_number']

class TeamMembersViewSet(viewsets.ModelViewSet):
     queryset = TeamMembers.objects.all()
     serializer_class = TeamMembersSerializer
     http_method_names = ['get','post','retrieve','put','patch']

     @action(detail=False, methods=['get'], renderer_classes=(TeamMemberListRenderer, ))
     def export_team_list(self, request, pk=None):
          order = TeamMembers.objects.all()
          serializer = TeamMembersSerializer(order, many=True)
          return Response(serializer.data)


@api_view(['GET'])
def get_my_team(request):
     # print("request")
     member = get_object_or_404(Team,owner=request.user.id)
     company = CompanyInformation.objects.get(team=member.pk)
     # serializer = CompanyInformationSerializer(company)
     serializer = TeamSerializer(member)
     return Response(serializer.data)


@api_view(['PUT','POST'])
def register_user(request):
     user = User.objects.create_user(**request.data)
     serializer = UserSerializer(user)
     new_user = authenticate(email=request.POST.get('email'),
            password=request.POST.get('password'),
            )
     if new_user is not None:
          if new_user.is_active:
               login(request, new_user)
     return Response(serializer.data)