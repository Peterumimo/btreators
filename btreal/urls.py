
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('listings/',include('listings.urls')),
    path('accounts/',include('accounts.urls')),
    path('contacts/',include('contacts.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
