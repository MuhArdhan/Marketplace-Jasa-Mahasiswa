from django.urls import path
from . import views

urlpatterns = [
    path("shop/", views.shop, name="shop"),
    path("product/<int:id>/", views.product_page, name="product_page"),
    path('dashboard-seller/', views.dashboard_seller, name='dashboard_seller'),
    path("jasa/add/", views.add_jasa, name="add_jasa"),
    path("jasa/edit/<int:jasa_id>/", views.update_jasa, name="update_jasa"),
    path("jasa/delete/<int:jasa_id>/", views.delete_jasa, name="delete_jasa"),
]
