from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils import timezone



class ProductInvertory(models.Model):
    product = models.OneToOneField('product.Product', verbose_name=_("product"), on_delete=models.CASCADE,related_name="invetory")
    quantity = models.IntegerField()
    lowcount = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _("Invertory")
        verbose_name_plural = _("Invertories")

    def __str__(self):
        return self.product.productName

    def get_absolute_url(self):
        return reverse("ProductInvertory_detail", kwargs={"pk": self.pk})