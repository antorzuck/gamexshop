from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('view-product', product_view),

    path('signup', signup)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
