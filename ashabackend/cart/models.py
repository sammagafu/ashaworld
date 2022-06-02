from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.conf import settings


class Cart(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=_("product"), on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Cart Owner"), on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name=_("Quantity"))
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    class Meta:
        verbose_name = _("Shopping Cart")
        verbose_name_plural = _("Shopping Cart")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
