from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # About
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),

    # Contact
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),

    # Shop list
    path('shop/', TemplateView.as_view(template_name='shop.html'), name='shop'),

    # Product detail page
    path('product/', TemplateView.as_view(template_name='productpage.html'), name='product_page'),

    # Login & Register
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),

    # Dashboard Seller
    path('dashboard-seller/', 
         TemplateView.as_view(template_name='dashboardseller.html'), 
         name='dashboard_seller'),

    # Add Product
    path(
        'dashboard-seller/add-product/',
        TemplateView.as_view(template_name='addproduct.html'),
        name='addproduct'
    ),

    # Edit Product
    path(
        'dashboard-seller/edit-product/',
        TemplateView.as_view(template_name='editproduct.html'),
        name='editproduct'
    ),

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
