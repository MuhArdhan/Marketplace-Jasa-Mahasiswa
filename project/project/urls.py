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
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('transactions/', include('transactions.urls')),
    path('', views_home.home, name='home'),

    # About
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),

    # Contact
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # Shop list
    path('', include('services.urls')),


    # # Login & Register
    # path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    # path('cstregister/', TemplateView.as_view(template_name='customer_register.html'), name='customer_register'),
    # path('register/', TemplateView.as_view(template_name='register.html'), name='register'),

    # Dashboard Seller
    # path('dashboard-seller/', 
    #      TemplateView.as_view(template_name='dashboardseller.html'), 
    #      name='dashboard_seller'),
    path('', include('services.urls')),


    # # Add Product
    # path(
    #     'dashboard-seller/add-product/',
    #     TemplateView.as_view(template_name='addproduct.html'),
    #     name='addproduct'
    # ),

    # # Edit Product
    # path(
    #     'dashboard-seller/edit-product/',
    #     TemplateView.as_view(template_name='editproduct.html'),
    #     name='editproduct'
    # ),

    # Dashboard Admin
    path('dashboard-admin/', 
         TemplateView.as_view(template_name='dashboardadmin.html'), 
         name='dashboard_admin'),

    path('transactions/', include('transactions.urls')),

]

# Supaya file static (CSS, JS, IMG) bisa diakses saat DEBUG=True
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
