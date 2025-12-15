from django.urls import path
from . import views

urlpatterns = [

    # Login & Register
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('register_cst/', views.register_customer, name='register_customer'),
    path('register_vndr/', views.register_vendor, name='register_vendor'),
]