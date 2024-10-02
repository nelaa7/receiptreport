from django.shortcuts import render, redirect
from .models import Kendaraan, Naker
# from .forms import form_kendaraan
from django.contrib import messages
import logging

# View Finance
def dashboard_admin(request):
    return render(request, 'finance/dashboard.html')

def report_admin_bbm(request):
    return render(request, 'finance/report/bbm.html')


# View Teknisi
def dashboard_teknisi(request):
    return render(request, 'teknisi/dashboard-teknisi.html')  

def progress_teknisi(request):
    return render(request, 'teknisi/progress.html')  

def data_naker(request):
    return render(request, 'finance/management/naker.html') 

def add_naker(request):
    return render(request, 'finance/management/add-naker.html') 


































# def add_kendaraan(request):
#     if request.method == 'POST':
#         form = form_kendaraan(request.POST, request.FILES)
#         if form.is_valid():
#             kendaraan = form.save(commit=False)
#             if hasattr(request.user, 'naker'):
#                 kendaraan.nik = request.user.naker
#             kendaraan.save()
#             return redirect('list-kendaraan')
#     else:
#         initial_data = {}
#         if hasattr(request.user, 'naker'):
#             initial_data['nik'] = request.user.naker
#         form = form_kendaraan(initial=initial_data)
    
#     context = {'form': form}
#     return render(request, 'leader/kendaraan/add-kendaraan.html', context)
















logger = logging.getLogger(__name__)

def form_kendaraan(request):
    if request.method == 'POST':
        logger.debug("POST request received")
        # Lanjutkan dengan penanganan form
    else:
        logger.debug("GET request received")










def form_kendaraan(request):
    nik = request.user.naker.nik if hasattr(request.user, 'Naker') else ''
    jenis_kbm_choices = Kendaraan.JENIS_KBM_CHOICES
    
    if request.method == 'POST':
        # nik = request.POST.get('nik')
        nik_instance = Naker.objects.get(nik=nik) 
        merk_type_option = request.POST.get('merk_type_option')  # Menangkap nilai radio button
        merk_type_kbm = request.POST.get('merk_type_kbm')  # nilai text area
        nik_pengguna_kbm_value = request.POST.get('nik_pengguna_kbm')
        try:
            # Ambil instance Naker berdasarkan nik
            nik_pengguna_kbm_instance = Naker.objects.get(nik=nik_pengguna_kbm_value)
        except Naker.DoesNotExist:
            messages.error(request, "NIK pengguna tidak ditemukan.")
            return redirect('form-kendaraan')
        no_polisi = request.POST.get('no_polisi') 
        odometer = request.POST.get('odometer')
        foto_odometer = request.FILES.get('foto_odometer')  
        foto_depan = request.FILES.get('foto_depan')  
        foto_samping = request.FILES.get('foto_samping')
        tgl_stnk = request.POST.get('tgl_stnk')
        tgl_service = request.POST.get('tgl_service')
        kondisi_kendaraan = request.POST.get('kondisi_kendaraan')
        foto_kondisi = request.FILES.get('foto_kondisi')

        # Menentukan merk_type yang digunakan
        merk_type = merk_type_kbm if merk_type_kbm else merk_type_option
        
        # Menyimpan data ke database
        Kendaraan.objects.create(
            # nik=nik,
            # nik=Naker.objects.get(id=nik_pengguna_kbm),
            nik=nik_instance,
            merk_type_KBM=merk_type,     
            nik_pengguna_kbm=nik_pengguna_kbm_instance,
            no_polisi=no_polisi,
            odometer=odometer,
            foto_speedometer=foto_odometer,
            foto_tampak_depan=foto_depan,
            foto_tampak_samping=foto_samping,
            tgl_tempo_STNK_5thn=tgl_stnk,
            tgl_service_terakhir=tgl_service,
            kondisi_kendaraan=kondisi_kendaraan,
            foto_kondisi_kendaraan=foto_kondisi
        )

        # Redirect ke halaman sukses atau halaman lain setelah menyimpan
        messages.success(request, "Kendaraan added successfully")
        return redirect('list-kendaraan')  # Ganti dengan URL yang sesuai


    # Jika bukan POST, ambil pilihan merk_type_kbm dari model
    merk_type_choices = Kendaraan.MERK_TYPE_KBM    
    context = {
        'witel_choices': Kendaraan.WITEL_CHOICES,
        # 'nik': nik,
        'jenis_kbm_choices': jenis_kbm_choices,
        'merk_type_choices': merk_type_choices,
    }
    return render(request, 'leader/kendaraan/form-kendaraan.html', context)

def list_kendaraan(request):
    return render(request, 'leader/kendaraan/list-kendaraan.html')

# def form_kendaraan(request):
#     witel_choices = Kendaraan.WITEL_CHOICES 
#     nik = request.user.naker.nik if hasattr(request.user, 'naker') else ''


#     return render(request, 'leader/kendaraan/form-kendaraan.html'),{
#     'witel_choices': witel_choices

        
#     }


