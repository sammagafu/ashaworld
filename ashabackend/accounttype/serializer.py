from dataclasses import fields
from rest_framework import serializers
from . models import CompanyInformation, Team, TeamMembers

class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = ['member','can_edit','admin']
        depth = 1

class TeamSerializer(serializers.ModelSerializer):
    teammember = TeamMembersSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['id','teamname','company','owner','teammember']
        depth = 1

class CompanyInformationSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True,read_only=True)

    class Meta:
        model = CompanyInformation
        fields = ['id','companyName','slug','relationship','city','country','phone_number','address','businessType','businessLincese','tin','businessLincese','team']
