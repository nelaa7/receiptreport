from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Sto (models.Model):
    id = models.AutoField(primary_key=True)
    nama_sto = models.CharField(max_length=255)
    
    create_at = models.DateTimeField( auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
       
    class Meta:
        verbose_name = 'STO'
        verbose_name_plural = 'STO'

    def __str__(self):
        return self.nama_sto
    
    
class Posisi (models.Model):
    POSISI_CHOICES = [
        ('Manager', 'Manager'),
        ('AssMAN','AssMAN'),
        ('Supervisor', 'Supervisor'),
        ('Team Leader', 'Team Leader'),
        ('Staff', 'Staff'),
        ('Helpdesk', 'Helpdesk'),
        ('Teknisi', 'Teknisi'),
    ]
    
    id = models.AutoField(primary_key=True)
    jenis_posisi = models.CharField(max_length=225, choices=[
        ('Manager', 'Manager'),
        ('AssMAN','AssMAN'),
        ('Supervisor', 'Supervisor'),
        ('Team Leader', 'Team Leader'),
        ('Staff', 'Staff'),
        ('Helpdesk', 'Helpdesk'),
        ('Teknisi', 'Teknisi'),
    ], default='Pilih Posisi')
    nama_posisi = models.CharField(max_length=225)

    create_at = models.DateTimeField( auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
       
    class Meta:
        verbose_name = 'Posisi'
        verbose_name_plural = 'Posisi'

    def __str__(self):
        return self.nama_posisi
    
    
class Project (models.Model):
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
    NOTA_CHOICES = [
        ('BBM', 'BBM'),
        ('Non-BBM', 'Non-BBM'),
    ]
    jenis_nota = models.CharField(max_length=255, choices=[('BBM', 'BBM'),('Non-BBM', 'Non-BBM')], default='default_value' )
    nama_nota = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'JenisNota'
        verbose_name_plural = 'JenisNota'

    def __str__(self):
        return self.nama_nota
    
    
class Role(models.Model):
    nama_role = models.CharField(max_length=255, )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Role'

    def __str__(self):
        return self.nama_role
    

class Naker(models.Model):
    WITEL_CHOICES = [
        ('Malang', 'Malang'),
        ('Kediri', 'Kediri'),
        ('Madiun', 'Madiun'),
    ]
    
    nik = models.CharField(max_length=255, primary_key=True)
    sto = models.ForeignKey('Sto', on_delete=models.CASCADE)
    posisi = models.ForeignKey('Posisi', on_delete=models.CASCADE)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, default='default_value')
    nama = models.CharField(max_length=255)
    witel = models.CharField(max_length=50, choices=[('Malang', 'Malang'), ('Kediri', 'Kediri'), ('Madiun', 'Madiun')])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Naker'
        verbose_name_plural = 'Naker'

    def __str__(self): 
        return self.nik
    
class MyUserManager(BaseUserManager):
    def create_user(self, Naker, password=None):
        if not Naker:
            raise ValueError('Users must have a NIK')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(Naker=Naker)
        user.set_password(password)
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    nik = models.OneToOneField(Naker, on_delete=models.CASCADE, related_name='users', null=True, blank=True, unique=True)
    # Email hanya akan diisi saat lupa password
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    
    objects = MyUserManager()
    USERNAME_FIELD = 'nik'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.Naker.nik)
    

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
    
    MERK_TYPE_KBM = [
        ('Honda Beat', 'Honda Beat'),
        ('Mitsubishi Expander', 'Mitsubishi Expander'),
    ]

    id = models.AutoField(primary_key=True)
    nik = models.ForeignKey(Naker,to_field='nik' ,on_delete=models.CASCADE, related_name='kendaraan_nik')
    tgl_pendataan = models.DateTimeField(auto_now_add=True)
    witel = models.CharField(max_length=10, choices=WITEL_CHOICES)
    jenis_KBM = models.CharField(max_length=2, choices=JENIS_KBM_CHOICES)
    merk_type_KBM = models.CharField(max_length=100, choices=MERK_TYPE_KBM)
    nik_pengguna_kbm = models.ForeignKey(Naker, on_delete=models.CASCADE, related_name='kendaraan_pengguna')
    no_polisi = models.CharField(max_length=20)
    odometer = models.CharField(max_length=20)
    foto_speedometer = models.ImageField(upload_to='speedometers/')
    foto_tampak_depan = models.ImageField(upload_to='kendaraan/depan/')
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
        return f'{self.merk_type_KBM} ({self.no_polisi})'
    

class Natura(models.Model):
    WITEL_CHOICES = [
        ('Malang', 'Malang'),
        ('Kediri', 'Kediri'),
        ('Madiun', 'Madiun'),
    ]

    id = models.AutoField(primary_key=True)
    nik = models.ForeignKey(Naker, to_field='nik', on_delete=models.CASCADE)
    nama = models.CharField(max_length=255, blank=True, null=True)
    posisi = models.ForeignKey('Posisi', on_delete=models.CASCADE)
    witel = models.CharField(max_length=10, choices=WITEL_CHOICES)
    km_referensi = models.DecimalField(max_digits=10, decimal_places=2)
    km_liter = models.DecimalField(max_digits=10, decimal_places=2)
    harga_bensin = models.DecimalField(max_digits=10, decimal_places=2)
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
    nik = models.ForeignKey(Naker, to_field='nik', on_delete=models.CASCADE)
    id_sto = models.ForeignKey(Sto, on_delete=models.CASCADE)
    id_jenis_nota = models.ForeignKey(JenisNota, on_delete=models.CASCADE)
    tgl_nota = models.DateField()
    jenis_KBM = models.CharField(max_length=2, choices=JENIS_KBM_CHOICES)
    no_polisi = models.CharField(max_length=20)
    km = models.CharField(max_length=20)
    nominal = models.IntegerField()
    foto_nota = models.ImageField(upload_to='notas/')
    foto_odo = models.ImageField(upload_to='odos/')
    uraian_kegiatan = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Proccessed')
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
    nik = models.ForeignKey(Naker, to_field='nik', on_delete=models.CASCADE)
    sto = models.ForeignKey(Sto, on_delete=models.CASCADE)
    jenis_nota = models.ForeignKey(JenisNota, on_delete=models.CASCADE)
    tgl_nota = models.DateField(null=True, blank=True)
    nominal = models.IntegerField()
    foto_nota = models.ImageField(upload_to='notas/')
    foto_evidence = models.ImageField(upload_to='evidences/')
    uraian_kegiatan = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Proccessed')
    status_changed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'TransaksiNonBBM'
        verbose_name_plural = 'TransaksiNonBBM'

    def __str__(self):
        return f'TransaksiNonBBM {self.id} - {self.nik}'
    
    