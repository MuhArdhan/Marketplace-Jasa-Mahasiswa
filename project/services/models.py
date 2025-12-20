from django.db import models

from users.models import Customer, Vendor

class Jasa(models.Model):
    id_jasa = models.AutoField(primary_key=True)
    vendor_id_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) 
    name_jasa = models.CharField(max_length=255)
    image = models.ImageField(upload_to='jasa_images/')
    harga = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deskripsi = models.TextField()
    status = models.CharField(max_length=50, default='Published')
    rating = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name_jasa

    class Meta:
        verbose_name_plural = 'Jasa'


class Review(models.Model):
    id_review = models.AutoField(primary_key=True)
    customer_idcustomer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    jasa_id_jasa = models.ForeignKey(Jasa, on_delete=models.CASCADE)
    komentar = models.TextField()
    rating = models.IntegerField()
    tanggal = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.jasa_idjasa.name_jasa}'

    class Meta:
        verbose_name_plural = 'Reviews'
