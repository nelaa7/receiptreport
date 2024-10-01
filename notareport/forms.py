from django.forms import ModelForm
from .models import Kendaraan

class form_kendaraan(ModelForm):
    class Meta:
        model = Kendaraan
        fields = '__all__'