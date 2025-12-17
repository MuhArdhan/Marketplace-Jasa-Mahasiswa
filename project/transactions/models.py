from django.db import models

from users.models import Customer
from services.models import Jasa

import datetime

class Transaction(models.Model):
    id_transaction = models.AutoField(primary_key=True)
    no_transaksi = models.CharField(max_length=20, unique=True, blank=True, editable=False)
    
    customer_id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    jasa_id_jasa = models.ForeignKey(Jasa, on_delete=models.SET_NULL, null=True)
    
    nominal = models.DecimalField(max_digits=10, decimal_places=2)
    deskripsi = models.TextField()
    tanggal = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        # Cek apakah ini data baru (belum punya no_transaksi)
        if not self.no_transaksi:
            today = datetime.date.today()
            current_year = today.year
            prefix = f"TRX-{current_year}"
            last_trx = Transaction.objects.filter(no_transaksi__startswith=prefix).order_by('-no_transaksi').first()
            
            if last_trx:
                last_number = int(last_trx.no_transaksi.split('-')[-1])
                new_number = last_number + 1
            else:
                new_number = 1

            self.no_transaksi = f"{prefix}-{new_number:03d}"
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Trx {self.id_transaction} - {self.nominal}"

    class Meta:
        verbose_name_plural = 'Transactions'
        
class Payment(models.Model):
    id_payment = models.AutoField(primary_key=True)
    transaction_id_transaksi = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    tanggal = models.DateField(auto_now_add=True)
    jenis_transaksi = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.no_transaksi

    class Meta:
        verbose_name_plural = 'Payments'

        
        
        
        
        