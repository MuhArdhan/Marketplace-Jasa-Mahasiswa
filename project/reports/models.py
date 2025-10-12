from django.db import models

from project.users.models import Customer, Vendor

class Aduan(models.Model):
    id_aduan = models.AutoField(primary_key=True)
    customer_id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vendor_id_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()
    image = models.ImageField(upload_to='aduan_images/')
    tanggal = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name_plural = 'Aduan'