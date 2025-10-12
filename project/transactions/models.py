from django.db import models

from project.users.models import Customer

class Payment(models.Model):
    id_payment = models.AutoField(primary_key=True)
    customer_id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    no_transaksi = models.CharField(max_length=255)
    tanggal = models.DateField(auto_now_add=True)
    jenis_transaksi = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.no_transaksi

    class Meta:
        verbose_name_plural = 'Payments'
