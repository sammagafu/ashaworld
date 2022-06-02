from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from django_resized import ResizedImageField

class Product(models.Model):
    productName = models.CharField(_("Product Name"),max_length=160)
    slug = models.SlugField(_("slug"),editable=False,unique=True,null=False)
    coverImage = ResizedImageField(upload_to = 'product/cover/%Y/%m/%d',verbose_name=_("cover Image"),size=[200, 400], crop=['middle', 'center'])
    brand = models.ForeignKey("brand.Brand", verbose_name=_("brand"), on_delete=models.SET_NULL,null=True,blank=True)
    category = models.ForeignKey("category.ProuctCategory", verbose_name=_("category"), on_delete=models.SET_NULL,null=True,blank=True)
    subCategory = models.ManyToManyField("category.ProductSubCategory")
    descripton = models.TextField(_("Product description"))
    sku = models.CharField(max_length=50,verbose_name=_("Stock Keeping Unit"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="normal Price")
    wholeSalePrice = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="wholesale Price") #when 20 products are bought 
    stock = models.ForeignKey("invetory.ProductInvertory", verbose_name=_("Number of Invetory"),related_name="stock", on_delete=models.SET_NULL,null=True,blank=True)
    discount = models.ForeignKey("product.ProductDiscount", verbose_name=_("discount in %"), related_name="productDicount", on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now,editable=False)
    modified_at = models.DateTimeField(blank=True,null=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

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

class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE,related_name="images")
    images = ResizedImageField(upload_to = 'product/images/%Y/%m/%d',verbose_name=_("Other Product Images"),size=[800, 900], crop=['middle', 'center'])

    def get_thumbnail(self):
        if self.images:
            return self.images.url
        else:
            if self.images:
                self.images = self.make_thumbnail(self.images)
                self.save()

                return self.images.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(500, 500)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        images = File(thumb_io, name=image.name)
        return images
        

class ProductReview(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=_("product"), on_delete=models.CASCADE)
    review = models.TextField(_("Product Review"))
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)

    class Meta:
        verbose_name = _("Product Review")
        verbose_name_plural = _("Product Reviews")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProductReview_detail", kwargs={"pk": self.pk})


class ProductRating(models.Model):
    product = models.ForeignKey("product.Product", verbose_name=_("Product"), on_delete=models.CASCADE)
    rating = models.IntegerField()
    rater = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)

    class Meta:
        verbose_name = _("Product Rating")
        verbose_name_plural = _("Product Ratings")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ProductRating_detail", kwargs={"pk": self.pk})



class ProductDiscount(models.Model):
    product = models.OneToOneField("product.Product", verbose_name=_("product"), on_delete=models.CASCADE,related_name="discountedProduct")
    discountName = models.CharField(max_length=130)
    descountPercentage = models.DecimalField(max_digits=2, decimal_places=2)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    expired_at = models.DateTimeField(blank=True,null=True)
    

    class Meta:
        verbose_name = _("Product Discount")
        verbose_name_plural = _("Product Discounts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("DiscountModel_detail", kwargs={"pk": self.pk})

    
