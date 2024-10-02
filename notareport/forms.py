from django.forms import ModelForm
from django import forms
from .models import Kendaraan, MyUser, Naker, Sto, Posisi, Unit, Role, Natura, JenisNota

class form_kendaraan(ModelForm):
    class Meta:
        model = Kendaraan
        fields = ['nik', 'witel', 'jenis_KBM', 'merk_type_KBM', 'nik_pengguna_kbm', 'no_polisi', 'odometer', 
                  'foto_speedometer', 'foto_tampak_depan', 'foto_tampak_samping', 'tgl_tempo_STNK_5thn', 
                  'tgl_service_terakhir', 'kondisi_kendaraan', 'foto_kondisi_kendaraan']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['witel'].widget = forms.Select(choices=Kendaraan.WITEL_CHOICES)
        self.fields['jenis_KBM'].widget = forms.Select(choices=Kendaraan.JENIS_KBM_CHOICES)
        

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['nik', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nik'].queryset = Naker.objects.all()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

        
        
class PasswordResetForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email tidak terdaftar.")
        return email
    
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
class FormAddNaker(forms.ModelForm):
    witel = forms.ChoiceField(choices=Naker.WITEL_CHOICES)
    
    class Meta:
        model = Naker
        fields = ['nik', 'nama', 'witel', 'sto', 'posisi', 'unit', 'role']  
    
    # Jika Anda ingin menampilkan pilihan tertentu, Anda bisa melakukannya di sini
    def __init__(self, *args, **kwargs):
        super(FormAddNaker, self).__init__(*args, **kwargs)
        self.fields['sto'].queryset = Sto.objects.all()
        self.fields['posisi'].queryset = Posisi.objects.all()
        self.fields['unit'].queryset = Unit.objects.all()
        self.fields['role'].queryset = Role.objects.all()
        
        
class FormAddNatura(forms.ModelForm):
    witel = forms.ChoiceField(choices=Natura.WITEL_CHOICES)
    
    class Meta:
        model = Natura
        fields = ['nik', 'nama', 'posisi', 'witel', 'km_referensi', 'km_liter', 'harga_bensin']
 
 
class FormAddNota(forms.ModelForm):

    class Meta:
        model = JenisNota
        fields = ['nama_nota']
  
  
class FormAddPosisi(forms.ModelForm):

    class Meta:
        model = Posisi
        fields = ['nama_posisi']
      
        









