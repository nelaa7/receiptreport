from django.forms import ModelForm
from django import forms
from .models import Kendaraan

class form_kendaraan(ModelForm):
    class Meta:
        model = Kendaraan
        fields = ['nik', 'witel', 'jenis_KBM', 'merk_type_KBM', 'NIK_pengguna_KBM', 'no_polisi', 'odometer', 
                  'foto_speedometer', 'foto_tampak_depan', 'foto_tampak_samping', 'tgl_tempo_STNK_5thn', 
                  'tgl_service_terakhir', 'kondisi_kendaraan', 'foto_kondisi_kendaraan']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['witel'].widget = forms.Select(choices=Kendaraan.WITEL_CHOICES)
        self.fields['jenis_KBM'].widget = forms.Select(choices=Kendaraan.JENIS_KBM_CHOICES)