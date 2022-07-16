from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify
from django.db.models.signals import post_save


# Create your models here.



relationshipToBusiness = [
    ("Junior Employee","Junior Employee"),
    ("Senior Employee","Senior Employee"),
    ("Approved Representative","Approved Representative"),
    ("Owner","Owner")
]

ACCOUNTTYPE = [
    ("Manufacture","Manufacture"),
    ("Reseller","Reseller"),
]

businessStatus = [
    ("Registered","Registered"),
    ("Not Registered","Not Registered"),
]

businessStatus = [
    ("Registered","Registered"),
    ("Not Registered","Not Registered"),
]

class CompanyInformation(models.Model):
    companyName = models.CharField(_("Manufacture Name"),max_length=160)
    slug = models.SlugField(_("slug"),editable=False,unique=True,null=False)
    accounttype = models.CharField(max_length=50,choices=ACCOUNTTYPE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    relationship = models.CharField(max_length=50,choices=relationshipToBusiness,default="Junior Employee",verbose_name=_("Relationship to Business"))
    city = models.CharField(verbose_name=_("City"), max_length=50)
    country = models.CharField(verbose_name=_("Country"), max_length=50)
    phone_number = PhoneNumberField(verbose_name=_("Business Phone Number"))
    address = models.TextField(verbose_name=_("Business Address"))
    businessType = models.CharField(max_length=60, verbose_name=_("Business Type"),choices=businessStatus)
    businessLincese = models.FileField(verbose_name=_("Bussiness Lincence"),help_text=_("Upload Business Lincence"),upload_to="upload/businesslicense/",null=True,blank=True)
    tin = models.FileField(verbose_name=_("Tax Indentification"),help_text=_("Upload Tax Indentification"),upload_to="upload/tin/",null=True,blank=True)
    verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.companyName)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.companyName

class Team(models.Model):
    teamname = models.CharField(max_length=180,verbose_name=_("Team name"))
    company = models.ForeignKey(CompanyInformation, on_delete=models.SET_NULL, null=True, blank=True,related_name="team")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class TeamMembers(models.Model):
    team = models.ForeignKey(Team,on_delete=models.SET_NULL,related_name="teammember", null=True, blank=True)
    member = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="member")
    can_edit = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)