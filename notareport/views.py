from django.shortcuts import render, redirect
from .models import Kendaraan, Naker, MyUser, Sto, Posisi, Unit, Role
from .forms import form_kendaraan, PasswordResetForm, RegistrationForm, form_add_naker
from django.contrib import messages
from django.contrib.auth import authenticate
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
    witel_choices = Naker._meta.get_field('witel').choices
    sto_list = Sto.objects.all()  # ambil semua data STO
    posisi_list = Posisi.objects.all() # ambil semua data Posisi
    unit_list = Unit.objects.all() # ambil semua data Posisi
    role_list = Role.objects.all() # ambil semua data Posisi
    return render(request, 'finance/management/add-naker.html', {'witel_choices': witel_choices, 'sto': sto_list, 'posisi': posisi_list, 'unit': unit_list, 'role': role_list}) 

def add__data_naker(request):
    if request.method == 'POST':
        form = form_add_naker(request.POST)
        if form.is_valid():
            form.save()  # Simpan data ke database
            return redirect('success_page')  # Ganti dengan URL tujuan setelah berhasil
    else:
        form = form_add_naker()
    
    return render(request, 'your_template.html', {'form': form})

























































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




def register(request):
    if request.method == 'POST': 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registrasi berhasil! Silakan login.')
            return redirect('login')  # Ganti dengan URL login yang sesuai
        else:
            messages.error(request, 'Registrasi gagal. Silakan periksa form Anda.')

    else:
        form = RegistrationForm()

    return render(request, 'auth/signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        nik = request.POST.get("nik")
        password = request.POST.get("password")
        
        MyUser = authenticate(request, nik=nik, password=password)  
        
        if MyUser is not None:
            login(request, MyUser )
            return redirect('dashboard-admin')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
        
    return render(request, 'auth/signin.html')



# def password_reset(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             user = MyUser.objects.get(email=email)

#             # Buat token atau URL pemulihan di sini
#             # Misal, token bisa menggunakan `django.utils.crypto.get_random_string()`

#             # Kirim email pemulihan
#             send_mail(
#                 'Pemulihan Password',
#                 'Klik link berikut untuk mereset password: <link>',  # Tambahkan link yang sesuai
#                 settings.DEFAULT_FROM_EMAIL,
#                 [email],
#                 fail_silently=False,
#             )
#             return redirect('password_reset_done')  # Ganti dengan URL yang sesuai
#     else:
#         form = PasswordResetForm()
#     return render(request, 'password_reset.html', {'form': form})
















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


