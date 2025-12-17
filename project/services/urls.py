from django.urls import path
from . import views

urlpatterns = [
    path("shop/", views.shop, name="shop"),
    path("product/<int:id>/", views.product_page, name="product_page"),
]
