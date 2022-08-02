from django.contrib import admin
from django.urls import path,include
# static and media files
from django.conf import settings
from django.conf.urls.static import static
from accounttype.views import register_user

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(tf_urls)),
    # path('', include(tf_twilio_urls)),
    # path('account/', include('allauth.urls')),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
    path('api/v1/product/',include('product.urls')),
    path('api/v1/category/',include('category.urls')),
    path('api/v1/brand/',include('brand.urls')),
    path('api/v1/cart/',include('cart.urls')),
    path('api/v1/order/',include('order.urls')),
    path('api/v1/pos/',include('pointofsale.urls')),
    path('api/v1/company/',include('accounttype.urls')),
    path('api/v1/register-user/',register_user, name='register-user')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
