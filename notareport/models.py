from django.db import models

# Create your models here.

class sto (models.Model):
    id = models.AutoField(primary_key=True)
    nama_sto = models.CharField(max_length=255)
    
    create_at = models.DateTimeField( auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
       
    class Meta:
        verbose_name = 'STO'
        verbose_name_plural = 'STO'

    def __str__(self):
        return self.nama_sto
    
    
class posisi (models.Model):
    id = models.AutoField(primary_key=True)
    nama_posisi = models.CharField(max_length=225)

    create_at = models.DateTimeField( auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
       
    class Meta:
        verbose_name = 'Posisi'
        verbose_name_plural = 'Posisi'

    def __str__(self):
        return self.nama_posisi