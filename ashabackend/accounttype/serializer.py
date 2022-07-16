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
        fields = ['slug','relationship','city','country','phone_number','address','businessType','businessLincese','tin','businessLincese','team']
    # team = models.ForeignKey(Team,on_delete=models.SET_NULL,related_name="teammember", null=True, blank=True)
    # member = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="member")
    # can_edit = models.BooleanField(default=False)
    # admin = models.BooleanField(default=False)