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
    
    
class project (models.Model):
    id = models.AutoField(primary_key=True)
    id_project = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
       
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project'

    def __str__(self):
        return self.id_project
    
    
class Unit(models.Model):
    nama_unit = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Unit'
        verbose_name_plural = 'Unit'

    def __str__(self):
        return self.nama_unit 


class JenisNota(models.Model):
    nama_nota = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'JenisNota'
        verbose_name_plural = 'JenisNota'

    def __str__(self):
        return self.nama_nota
    

class Naker(models.Model):
    nik = models.CharField(max_length=255, primary_key=True)
    sto = models.ForeignKey('Sto', on_delete=models.CASCADE)
    posisi = models.ForeignKey('Posisi', on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    witel = models.CharField(max_length=50, choices=[('Malang', 'Malang'), ('Kediri', 'Kediri'), ('Madiun', 'Madiun')])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Naker'
        verbose_name_plural = 'Naker'

    def __str__(self): 
        return self.nik
    

class Kendaraan(models.Model):
    WITEL_CHOICES = [
        ('Malang', 'Malang'),
        ('Kediri', 'Kediri'),
        ('Madiun', 'Madiun'),
    ]

    JENIS_KBM_CHOICES = [
        ('R2', 'R2'),
        ('R4', 'R4'),
    ]

    id = models.AutoField(primary_key=True)
    nik = models.ForeignKey(Naker, on_delete=models.CASCADE)
    tgl_pendataan = models.DateTimeField(auto_now_add=True)
    witel = models.CharField(max_length=10, choices=WITEL_CHOICES)
    jenis_kbm = models.CharField(max_length=2, choices=JENIS_KBM_CHOICES)
    merk_type_kbm = models.CharField(max_length=100)
    NIK_pengguna_KBM = models.CharField(max_length=20)
    no_polisi = models.CharField(max_length=20)
    odometer = models.CharField(max_length=20)
    foto_speedometer = models.ImageField(upload_to='speedometers/')
    foto_tmpak_depan = models.ImageField(upload_to='kendaraan/depan/')
    foto_tampak_samping = models.ImageField(upload_to='kendaraan/samping/')
    tgl_tempo_STNK_5thn = models.DateField()
    tgl_service_terakhir = models.DateField()
    kondisi_kendaraan = models.CharField(max_length=100, null=True, blank=True)
    foto_kondisi_kendaraan = models.ImageField(upload_to='kendaraan/kondisi/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Kendaraan'
        verbose_name_plural = 'Kendaraan'
        
    def __str__(self):
        return f'{self.merk_type_kbm} ({self.no_polisi})'
    

class Natura(models.Model):
    WITEL_CHOICES = [
        ('Malang', 'Malang'),
        ('Kediri', 'Kediri'),
        ('Madiun', 'Madiun'),
    ]

    id = models.AutoField(primary_key=True)
    nik = models.ForeignKey(Naker, on_delete=models.CASCADE)
    id_posisi = models.ForeignKey(posisi, on_delete=models.CASCADE)
    witel = models.CharField(max_length=10, choices=WITEL_CHOICES)
    km_referensi = models.CharField(max_length=20)
    km_liter = models.CharField(max_length=20)
    harga_bensin = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Natura'
        verbose_name_plural = 'Natura' 
        
    def __str__(self):
        return f'Natura {self.id} - {self.km_referensi}'
    

class TransaksiBBM(models.Model):
    JENIS_KBM_CHOICES = [
        ('R2', 'R2'),
        ('R4', 'R4'),
    ]

    STATUS_CHOICES = [
        ('rejected', 'Rejected'),
        ('processed', 'Processed'),
        ('verified', 'Verified'),
        ('paid', 'Paid'),
    ]

    id = models.AutoField(primary_key=True)
    nik = models.ForeignKey(Naker, on_delete=models.CASCADE)
    id_sto = models.ForeignKey(sto, on_delete=models.CASCADE)
    id_jenis_nota = models.ForeignKey(JenisNota, on_delete=models.CASCADE)
    tgl_input = models.DateTimeField(null=True, blank=True)
    tgl_nota = models.DateField()
    jenis_kbm = models.CharField(max_length=2, choices=JENIS_KBM_CHOICES)
    no_polisi = models.CharField(max_length=20)
    km = models.CharField(max_length=20)
    nominal = models.IntegerField()
    foto_nota = models.ImageField(upload_to='notas/')
    foto_odo = models.ImageField(upload_to='odos/')
    uraian_kegiatan = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    status_changed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'TransaksiBBM'
        verbose_name_plural = 'TransaksiBBM'

    def __str__(self):
        return f'TransaksiBBM {self.id} - {self.no_polisi}'


class TransaksiNonBBM(models.Model):
    STATUS_CHOICES = [
        ('rejected', 'Rejected'),
        ('processed', 'Processed'),
        ('verified', 'Verified'),
        ('paid', 'Paid'),
    ]

    id = models.AutoField(primary_key=True)
    nik = models.ForeignKey(Naker, on_delete=models.CASCADE)
    sto = models.ForeignKey(sto, on_delete=models.CASCADE)
    jenis_nota = models.ForeignKey(JenisNota, on_delete=models.CASCADE)
    tgl_input = models.DateTimeField(auto_now_add=True)
    tgl_nota = models.DateField(null=True, blank=True)
    nominal = models.IntegerField()
    foto_nota = models.ImageField(upload_to='notas/')
    foto_evidence = models.ImageField(upload_to='evidences/')
    uraian_kegiatan = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    status_changed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'TransaksiNonBBM'
        verbose_name_plural = 'TransaksiNonBBM'

    def __str__(self):
        return f'TransaksiNonBBM {self.id} - {self.nik}'
    
    