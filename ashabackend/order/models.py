from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
import uuid 


STATUS = [
    ("Pending","Pending"),
    ("Cancelled","Cancelled"),
    ("Refunded","Refunded"),
    ("Disputed","Disputed"),
    ("Shipped","Shipped"),
    ("Paid","Paid"),
    ("Deliverd","Delivered")
]


class Order(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Order Owner"), on_delete=models.CASCADE, related_name="owner")
    slug = models.SlugField(_("slug"),editable=False,unique=True,null=False)
    orderstatus = models.CharField(max_length=50,choices=STATUS,default=STATUS[0][0])
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    paid_at = models.DateTimeField(verbose_name=_("Payment Date"), blank=True,null=True,editable=False)
    promo_code = models.CharField(max_length=50,null=True,blank=True)
    totalprice = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    active = models.BooleanField(_("Active Order"),default=True)
    


    def save(self,*args, **kwargs):
        if self.pk is None:
            self.slug = "asha-order-" + uuid.uuid4().hex[:12].lower()
        super(Order,self).save()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.slug


class OrderItems(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=_("product"),on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.CASCADE,related_name="orderproducts")
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(verbose_name=_("Product Quantity"), default=1)
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.product.productName

