from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from . import views as views_home

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', include('users.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('transactions/', include('transactions.urls')),
    path('', views_home.home, name='home'),

    # About
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),

    # Contact
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # Shop list
    path('', include('services.urls')),
]

# Supaya file static (CSS, JS, IMG) bisa diakses saat DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
