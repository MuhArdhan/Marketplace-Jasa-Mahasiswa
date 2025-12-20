from django.db import models

class Customer(models.Model):
    idcustomer = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    no_hp = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 
    status = models.CharField(max_length=50, default='aktif')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Customers'


class Vendor(models.Model):
    id_vendor = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    no_hp = models.CharField(max_length=15)
    rating = models.IntegerField(default=0)
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=50, default='Aktif')
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Vendors'


class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = 'Admins'
