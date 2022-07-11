from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField
from django.utils import timezone
from django.conf import settings
import uuid 
from django.utils.translation import gettext as _
from django.utils.text import slugify

# Create your models here.
class POSclient(models.Model):

    PAYMENT_METHODS = [
        ("CASH","CASH"),
        ("CARD","CARD"),
        ("MOBILE","MOBILE"),
    ]

    MNO = [
        ("Airtel Money","Airtel Money"),
        ("M-pesa","M-pesa"),
        ("Tigopesa","Tigopesa"),
    ]
    clients = models.CharField(max_length=50,verbose_name="Clients Full Name")
    clientsemail = models.EmailField(verbose_name="Clients Email")
    address = models.TextField()
    phone_number = PhoneNumberField(verbose_name="User Phone Number")
    payment = models.CharField(max_length=50, choices=PAYMENT_METHODS,default=PAYMENT_METHODS[0][0])
    provider = models.CharField(max_length=50,null=True,blank=True,verbose_name="Service Provider")
    company = models.ForeignKey("accounttype.CompanyInformation", verbose_name=_("Company Info"), on_delete=models.CASCADE,related_name="clientof")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Addeby"), on_delete=models.SET_NULL,null=True)
    isactive = models.BooleanField(default=True,null=True,blank=True)
    

    class Meta:
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Addresss'


class POSproduct(models.Model):
    productName = models.CharField(_("Product Name"),max_length=160)
    slug = models.SlugField(_("slug"),editable=False,unique=True,null=False)
    coverImage = ResizedImageField(upload_to = 'product/cover/%Y/%m/%d',verbose_name=_("cover Image"),size=[300, 350], crop=['middle', 'center'])
    brand = models.ForeignKey("brand.Brand", verbose_name=_("brand"), on_delete=models.SET_NULL,null=True,blank=True)
    category = models.ForeignKey("category.ProuctCategory", verbose_name=_("category"), on_delete=models.SET_NULL,null=True,blank=True)
    subCategory = models.ManyToManyField("category.ProductSubCategory")
    descripton = models.TextField(_("Product description"))
    sku = models.CharField(max_length=50,verbose_name=_("Stock Keeping Unit"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="normal Price")
    wholeSalePrice = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="wholesale Price") #when 20 products are bought 
    discount = models.ForeignKey("product.ProductDiscount", verbose_name=_("discount in %"), related_name="productdiscount", on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now,editable=False)
    modified_at = models.DateTimeField(blank=True,null=True)
    approved = models.BooleanField(default=False,verbose_name="Approved for POS")

    def __str__(self):
        return self.productName
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified_at = timezone.now()
        if not self.slug:
            self.slug = slugify(self.productName)
        self.slug = slugify(self.productName)
        return super().save()

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}'

    def get_coverImage(self):
        if self.coverImage:
            return 'https://api.asha-world.com' + self.coverImage.url
        return ''


class POSorder(models.Model):
    order = models.SlugField(_("order"),editable=False,unique=True,null=False)
    product = models.ForeignKey(POSproduct, verbose_name=_("product"), on_delete=models.CASCADE)
    buyer = models.ForeignKey(POSclient, verbose_name=_("product"), on_delete=models.SET_NULL,blank=True,null=True)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Seller"), on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
        if self.pk is None:
            self.slug = "asha-order" + uuid.uuid4().hex[:18].lower()
        super(POSproduct,self).save()
