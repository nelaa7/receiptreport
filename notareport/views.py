from django.shortcuts import render
from .models import Kendaraan

# View Finance
def dashboard_admin(request):
    return render(request, 'finance/dashboard.html')

def report_admin_bbm(request):
    return render(request, 'finance/report/bbm.html')
























def form_kendaraan(request):
    form = Kendaraan()
    nik = request.user.naker.nik if hasattr(request.user, 'naker') else ''
    jenis_kbm_choices = Kendaraan.JENIS_KBM_CHOICES
    context = {
        'form': form,
        'witel_choices': Kendaraan.WITEL_CHOICES,
        'nik': nik,
        'jenis_kbm_choices' : jenis_kbm_choices
    }
    return render(request, 'leader/kendaraan/form-kendaraan.html', context)


# def form_kendaraan(request):
#     witel_choices = Kendaraan.WITEL_CHOICES 
#     nik = request.user.naker.nik if hasattr(request.user, 'naker') else ''


#     return render(request, 'leader/kendaraan/form-kendaraan.html'),{
#     'witel_choices': witel_choices

        
#     }
