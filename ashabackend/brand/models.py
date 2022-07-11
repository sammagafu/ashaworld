from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils.text import slugify
from django_resized import ResizedImageField
from accounttype.models import CompanyInformation   

class Brand(models.Model):
    brandName = models.CharField(_("Brand Name"),max_length=160)
    manufacture = models.ForeignKey(CompanyInformation  , verbose_name=_("Product Manufacture"), on_delete=models.CASCADE)
    slug = models.SlugField(_("slug"),editable=False,unique=True,null=True)
    brandlogo =  ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='uploads/brands')
    description = models.TextField(_("Brand Description"))

    class Meta:
        verbose_name = _("brand")
        verbose_name_plural = _("brands")

    def __str__(self):
        return self.brandName
    
    def get_brandImg(self):
        if self.brandlogo:
            return 'https://api.asha-world.com' + self.brandlogo.url
        return ''

    def save(self):
        if not self.slug:
            self.slug = slugify(self.brandName)
        self.slug = slugify(self.brandName)
        super().save()
    
    
        

    # def get_absolute_url(self):
    #     return reverse("brand_detail", kwargs={"pk": self.pk})
