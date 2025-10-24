from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Halaman utama (Home)
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
     # Halaman Shop List
    path('shop/', TemplateView.as_view(template_name='shop_list.html'), name='shop'),
    # Halaman Shop Detail
    path('shop/detail/', TemplateView.as_view(template_name='shop_detail.html'), name='shop_detail'),
    path('', include('transactions.urls')),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),


]

# Supaya file static (CSS, JS, IMG) bisa diakses saat DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
