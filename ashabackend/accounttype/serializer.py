from dataclasses import fields
from rest_framework import serializers
from . models import CompanyInformation, Team, TeamMembers

class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = ['member','can_edit','admin','team']

class TeamSerializer(serializers.ModelSerializer):
    teammember = TeamMembersSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['teamname','company','owner','teammember']

class CompanyInformationSerializer(serializers.ModelSerializer):
    team = TeamSerializer(many=True,read_only=True)

    class Meta:
        model = CompanyInformation
        fields = ['id','companyName','slug','relationship','city','country','phone_number','address','businessType','businessLincese','tin','businessLincese','team']