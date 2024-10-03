import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Kendaraan, Naker, MyUser, Sto, Posisi, Unit, Role, JenisNota, Project, Natura, TransaksiBBM, TransaksiNonBBM
from .forms import form_kendaraan, PasswordResetForm, RegistrationForm, FormAddNaker, FormAddNatura, FormAddNota, FormAddPosisi
from django.contrib import messages 
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.db import close_old_connections, connections
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db.utils import OperationalError 
from django.template.loader import render_to_string 

import logging
from django.http import JsonResponse


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

def management_naker(request):
    nakers = Naker.objects.all()  # Fetch all naker data
    return render(request, 'finance/management/naker.html', {'nakers': nakers})

def add_naker(request):
    if request.method == 'POST':
        form = FormAddNaker(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management_naker')
    else:
        form = FormAddNaker()

    # Ambil witel_choices dari model
    witel_choices = Naker.WITEL_CHOICES

    return render(request, 'finance/management/add-naker.html', {
        'form': form,
        'witel_choices': witel_choices, 
        'sto': Sto.objects.all(),
        'posisi': Posisi.objects.all(),
        'unit': Unit.objects.all(),
        'role': Role.objects.all(),
    })
    
def add_natura(request):
    if request.method == 'POST':
        form = FormAddNatura(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management-natura')
    else:
        form = FormAddNatura()
        
    # Ambil witel_choices dari model
    witel_choices = Naker.WITEL_CHOICES

    return render(request, 'finance/management/add-natura.html', {
        'form': form,
        'posisi': Posisi.objects.all(),
        'witel_choices': witel_choices,
    })
    

def add_nota(request):
    if request.method == 'POST':
        form = FormAddNota(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management-nota')
    else:
        form = FormAddNota()

    return render(request, 'finance/management/add-nota.html')
    
    
def add_posisi(request):
    if request.method == 'POST':
        form = FormAddPosisi(request.POST)
        if form.is_valid():
            form.save()
            return redirect('management-posisi')
    else:
        form = FormAddPosisi()

    return render(request, 'finance/management/add-posisi.html')
    








































































































def naker_edit(request, pk):
    naker = get_object_or_404(Naker, id=pk)
    
    if request.method == 'POST':
        form = FormAddNaker(request.POST, instance=naker)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True}) #sukses
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400) #form ga valid
    else:
        form = FormAddNaker(instance=naker)    
    
    html = render_to_string (request, 'finance/management/naker.html' ,{'form':form} )
    return JsonResponse({'html': html})










def sto_list(request):
    sto_list = Sto.objects.all()
    context= {
        'sto_list':sto_list
    }
    return render(request, "finance/management/sto.html", context)

def sto_edit(request, id):
    sto_edit = get_object_or_404(Sto, id=id)
    if request.method == "POST":
        try:
            # nama_sto = json.loads(request.body) 
            sto_edit.id = request.POST.get('id', sto_edit.id) 
            sto_edit.nama_sto = request.POST.get('nama_sto', sto_edit.nama_sto)  
            sto_edit.save()  # Simpan perubahan ke database
            return JsonResponse({'message': 'Data updated successfully'}, status=200)
        except Exception as e:
            print(f'Error updating STO: {e}')  # Tambahkan logging untuk error
            return JsonResponse({'message': 'There was an error updating the data!'}, status=500)

    context = {
        'sto_edit': sto_edit
    }
    
    return render(request, "finance/management/sto.html", context)

def jenisNota_list(request):
    jenisNota_list = JenisNota.objects.all()
    context={
        'jenisNota_list':jenisNota_list
    }
    return render(request, "finance/management/nota.html", context)

def posisi_list(request):
    posisi_list = Posisi.objects.all()
    context={
        'posisi_list':posisi_list
    }
    return render(request, "finance/management/posisi.html", context)
def project(request):
    project = Project.objects.all()
    context={
        'project':project
    }
    return render(request, "finance/management/project.html", context)

# def naker_list(request):
#     naker_list=Naker.objects.all()
#     context={
#         'naker_list':naker_list
#     }
#     return render(request, "finance/management/naker.html", context)

def natura_list(request):
    natura_list=Natura.objects.all()
    context={
        'natura_list':natura_list
    }
    return render(request, "finance/management/natura.html", context)

def kendaraan_list(request):
    kendaraan_list=Kendaraan.objects.all()
    context={
        'kendaraan_list':kendaraan_list
    }
    return render(request, "finance/management/kendaraan.html", context)


def transaksiBBM_list(request):
    # Ambil role pengguna saat ini
    if hasattr(request.MyUser,'role'):
        nama_role = request.user.role.nama_role

    transaksi_list = TransaksiBBM.objects.all()
    
    if nama_role == 'Admin':
        template = 'finance/transaction/bbm.html'
    elif nama_role == 'Leader':
        template = 'finance/report/bbm.html'
    # elif nama_role = 'Teknisi':
    #     template = ''
    else:
        template = '' #yg ga ada role 
 
    context = {
        'transaksi_list': transaksi_list,
    }
    return render(request, template, context)
    










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


def check_database_connection(request):
    try:
        # Mencoba mendapatkan cursor dari koneksi default
        with connections['default'].cursor() as cursor:
            # Mencoba menjalankan query sederhana
            cursor.execute("SELECT 1")
            one = cursor.fetchone()[0]
            if one == 1:
                logger.info("Database connection successful")
                return JsonResponse({
                    'status': 'success',
                    'message': 'Database connection is working properly'
                })
            else:
                logger.error("Unexpected result from database query")
                return JsonResponse({
                    'status': 'error',
                    'message': 'Unexpected result from database'
                }, status=500)
    except OperationalError as e:
        logger.error(f"Database connection failed: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': 'Unable to connect to the database',
            'error': str(e)
        }, status=500)
    except Exception as e:
        logger.exception(f"Unexpected error during database check: {str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': 'An unexpected error occurred',
            'error': str(e)
        }, status=500)

def register_view(request):
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

@ensure_csrf_cookie
def login_view(request):
    close_old_connections()
    
    if request.method == "POST":
        nik = request.POST.get("nik")
        password = request.POST.get("password")
        
        if not nik or not password:
            logger.warning("Login attempt with missing credentials")
            return JsonResponse({'success': False, 'error': 'NIK and password are required'}, status=400)
        
        try:
            user = authenticate(request, nik=nik, password=password)
            
            if user is not None:
                login_view(request, user)
                logger.info(f"User {nik} logged in successfully")
                return JsonResponse({'success': True})
            else:
                logger.warning(f"Failed login attempt for NIK: {nik}")
                return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=401)
        
        except Exception as e:
            logger.exception(f"Error during login process: {str(e)}")
            return JsonResponse({'success': False, 'error': 'An error occurred during login'}, status=500)
        
        finally:
            close_old_connections()
    
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


