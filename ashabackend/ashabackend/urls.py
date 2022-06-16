from django.contrib import admin
from django.urls import path,include
# static and media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(tf_urls)),
    # path('', include(tf_twilio_urls)),
    # path('account/', include('allauth.urls')),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/',include('djoser.urls.authtoken')),
    path('api/v1/',include('product.urls')),
    path('api/v1/',include('category.urls')),
    path('api/v1/',include('brand.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
