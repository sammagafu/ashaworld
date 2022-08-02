from dataclasses import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from . models import CompanyInformation, Team, TeamMembers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['username', 'email', 'password']

    def create(self,validated_data):
        user = User.objects.all()[0]
        print(validated_data)
        return user


class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = ['member','can_edit','admin','team']
        depth=1

class TeamSerializer(serializers.ModelSerializer):
    teammember = TeamMembersSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['teamname','company','owner','teammember']
        # depth=1

class CompanyInformationSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True,read_only=True)

    class Meta:
        model = CompanyInformation
        # depth=1
        fields = ['id','companyName','slug','relationship','city','country','phone_number','address','businessType','businessLincese','tin','businessLincese','team']