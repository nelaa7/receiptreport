from django.forms import ModelForm
from django import forms
from .models import Kendaraan, MyUser, Naker, Sto, Posisi, Unit, Natura, JenisNota, Project, Role

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

    class Meta:
        model = Naker
        fields = ('nik', 'sto', 'posisi', 'unit', 'role', 'nama', 'witel')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nik'].widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'NIKNumber', 'name': 'NIKNumber'})  
        self.fields['nama'].widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'TextNama', 'name': 'TextNama'})  
        self.fields['witel'].widget = forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'id': 'WITELSelect',
            'data-control': 'select2',
            'data-dropdown-css-class': 'w-200px',
            'data-placeholder': 'Pilih witel',
            'data-hide-search': 'true'
        })
        self.fields['witel'].initial = 'Pilih WITEL'
        self.fields['witel'].choices = [('', 'Pilih WITEL')] + Naker.WITEL_CHOICES
        
        self.fields['sto'].widget = forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'id': 'STOSelect',
            'data-control': 'select2',
            'data-dropdown-css-class': 'w-200px',
            'data-placeholder': 'Pilih sto',
            'data-hide-search': 'false'
        })
        self.fields['sto'].empty_label = 'Pilih STO'
        self.fields['sto'].queryset = Sto.objects.all()
        
        self.fields['posisi'].widget = forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'id': 'PosisiSelect',
            'data-control': 'select2',
            'data-dropdown-css-class': 'w-200px',
            'data-placeholder': 'Pilih posisi',
            'data-hide-search': 'false'
        })
        self.fields['posisi'].empty_label = 'Pilih Posisi'
        self.fields['posisi'].queryset = Posisi.objects.all()
        
        self.fields['unit'].widget = forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'id': 'UnitSelect',
            'data-control': 'select2',
            'data-dropdown-css-class': 'w-200px',
            'data-placeholder': 'Pilih unit',
            'data-hide-search': 'false'
        })
        self.fields['unit'].empty_label = 'Pilih Unit'
        self.fields['unit'].queryset = Unit.objects.all()
        
        self.fields['role'].widget = forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'id': 'RoleSelect',
            'data-control': 'select2',
            'data-dropdown-css-class': 'w-200px',
            'data-placeholder': 'Pilih role',
            'data-hide-search': 'true'
        })
        self.fields['role'].empty_label = 'Pilih Role'
        self.fields['role'].queryset = Role.objects.all()
        
        
class FormAddNatura(forms.ModelForm):
    class Meta:
        model = Natura
        fields = ('nik', 'nama', 'posisi', 'witel', 'km_referensi', 'km_liter', 'harga_bensin')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama'].widget.attrs['readonly'] = True
        self.fields['posisi'].widget.attrs['readonly'] = True
        self.fields['witel'].widget.attrs['readonly'] = True
    
 
class FormAddNota(forms.ModelForm):

    class Meta:
        model = JenisNota
        fields = ('jenis_nota', 'nama_nota')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)          
        self.fields['jenis_nota'].widget = forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'id': 'NOTASelect',
            'data-control': 'select2',
            'data-dropdown-css-class': 'w-200px',
            'data-placeholder': 'Pilih jenis nota',
            'data-hide-search': 'true'
        })
        self.fields['jenis_nota'].empty_label = 'Pilih Jenis Nota'
        self.fields['jenis_nota'].choices = [('', 'Pilih Jenis Nota')] + JenisNota.NOTA_CHOICES
        self.fields['nama_nota'].widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'TextNota', 'name': 'TextNota'})
        
  
class FormAddPosisi(forms.ModelForm):

    class Meta:
        model = Posisi
        fields = ('jenis_posisi', 'nama_posisi')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jenis_posisi'].widget = forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'id': 'PosisiSelect',
            'data-control': 'select2',
            'data-dropdown-css-class': 'w-200px',
            'data-placeholder': 'Pilih jenis posisi',
            'data-hide-search': 'true'
        })
        self.fields['jenis_posisi'].empty_label = 'Pilih Jenis Posisi'
        self.fields['jenis_posisi'].choices = [('', 'Pilih Jenis Posisi')] + Posisi.POSISI_CHOICES
        self.fields['nama_posisi'].widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'TextPosisi', 'name': 'TextPosisi'})

class FormAddProject(forms.ModelForm):
    
    class Meta:
        model = Project
        fields = ['id_project']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_project'].widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'TextProject', 'name': 'TextProject'})


class FormAddSto(forms.ModelForm):
    
    class Meta:
        model = Sto
        fields = ['nama_sto']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nama_sto'].widget = forms.TextInput(attrs={'class': 'form-control', 'id': 'TextSTO', 'name': 'TextSTO'})


class FormAddKendaraan(forms.ModelForm):

    class Meta:
        model = Kendaraan
        fields = ['nik', 'witel', 'jenis_KBM', 'merk_type_KBM', 'nik_pengguna_kbm', 
                  'no_polisi', 'odometer', 'foto_speedometer', 'foto_tampak_depan', 
                  'foto_tampak_samping', 'tgl_tempo_STNK_5thn', 'tgl_service_terakhir', 
                  'kondisi_kendaraan', 'foto_kondisi_kendaraan']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nik'].widget = forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'NIKNumber', 
            'name': 'NIKNumber'
        })
        
        self.fields['witel'].widget = forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'id': 'WITELSelect',
            'data-control': 'select2',
            'data-dropdown-css-class': 'w-200px',
            'data-placeholder': 'Pilih area',
            'data-hide-search': 'true'
        })
        self.fields['witel'].initial = 'Pilih Area'
        self.fields['witel'].choices = [('', 'Pilih Area')] + Naker.WITEL_CHOICES
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nik'].widget = forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'NIKNumber', 
            'name': 'NIKNumber'
        })
        
        self.fields['witel'].widget = forms.Select(attrs={
            'class': 'form-select form-select-solid',
            'id': 'WITELSelect',
            'data-control': 'select2',
            'data-dropdown-css-class': 'w-200px',
            'data-placeholder': 'Pilih area',
            'data-hide-search': 'true'
        })
        self.fields['witel'].initial = 'Pilih Area'
        self.fields['witel'].choices = [('', 'Pilih Area')] + Naker.WITEL_CHOICES

        self.fields['jenis_KBM'].widget = forms.RadioSelect(attrs={
            'class': 'btn-group btn-group-solid',
            'id': 'jenis_KBM',
            'data-kt-buttons': 'true',
            'data-kt-buttons-target': '[data-kt-button="true"]'
        })
        self.fields['jenis_KBM'].choices = [
            ('roda2', 'Roda 2'),
            ('roda4', 'Roda 4')
        ]

        self.fields['merk_type_KBM'].widget = forms.RadioSelect(attrs={
            'class': 'btn-group btn-group-solid',
            'id': 'merk_type_KBM',
            'data-kt-buttons': 'true',
            'data-kt-buttons-target': '[data-kt-button="true"]'
        })
        self.fields['merk_type_KBM'].choices = [
            ('honda_beat', 'Honda Beat'),
            ('mitsubishi_expander', 'Mitsubishi Expander'),
            ('lainnya', 'Yang lain')
        ]

        self.fields['nik_pengguna_kbm'].widget = forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'NIKNumberPengguna', 
            'name': 'NIKNumberPengguna'
        })

        self.fields['no_polisi'].widget = forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'plateNumber', 
            'name': 'plateNumber'
        })

        self.fields['odometer'].widget = forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'odometer', 
            'name': 'odometer'
        })

        self.fields['foto_speedometer'].widget = forms.FileInput(attrs={
            'class': 'form-control', 
            'id': 'speedometerPhoto', 
            'name': 'speedometerPhoto'
        })

        self.fields['foto_tampak_depan'].widget = forms.FileInput(attrs={
            'class': 'form-control', 
            'id': 'foto_tampak_depan', 
            'name': 'foto_tampak_depan'
        })

        self.fields['foto_tampak_samping'].widget = forms.FileInput(attrs={
            'class': 'form-control', 
            'id': 'foto_tampak_samping', 
            'name': 'foto_tampak_samping'
        })

        self.fields['tgl_tempo_STNK_5thn'].widget = forms.DateInput(attrs={
            'class': 'form-control', 
            'id': 'tanggalJatuhTempo', 
            'name': 'tanggalJatuhTempo'
        })

        self.fields['tgl_service_terakhir'].widget = forms.DateInput(attrs={
            'class': 'form-control', 
            'id': 'tanggalServiceTerakhir', 
            'name': 'tanggalServiceTerakhir'
        })

        self.fields['kondisi_kendaraan'].widget = forms.TextInput(attrs={
            'class': 'form-control', 
            'id': 'vehicleCondition', 
            'name': 'vehicleCondition'
        })

        self.fields['foto_kondisi_kendaraan'].widget = forms.FileInput(attrs={
            'class': 'form-control', 
            'id': 'vehiclePhoto', 
            'name': 'vehiclePhoto'
        })  
        
