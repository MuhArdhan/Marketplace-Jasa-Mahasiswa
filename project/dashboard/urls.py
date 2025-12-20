from django.urls import path
from . import views

urlpatterns = [
    # Dashboard Admin
    path('dashboard-admin/', views.dashboard_admin_view, name='dashboard_admin'),

    # Dashboard Seller
    path('dashboard-seller/', views.dashboard_seller_view, name='dashboard_seller'),

    # Update Listing Data
    path('update-listing/', views.update_listing_jasa, name='update_listing_jasa'),   
     
    # Add Product
    path('dashboard-seller/add-product/', views.add_product_view, name='addproduct'),

    # Edit Product
    path('dashboard-seller/edit-product/', views.edit_product_view, name='editproduct'),
    
    path('api/update-status-jasa/', views.update_status_jasa, name='update_status_jasa'),
    path('api/update-status-user/', views.update_status_user, name='update_status_user'),    
]
