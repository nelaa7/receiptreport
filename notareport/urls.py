from django.urls import path
from.import views

urlpatterns = [
    path('dashboard-admin/', views.dashboard_admin, name='dashboard_admin'),
    path('report-bbm/', views.report_admin_bbm, name='report_bbm'),
    # path('form-kendaraan/', views.form_kendaraan, name='form-kendaraan'),
    path('list-kendaraan/', views.list_kendaraan, name='kendaraan_list'),
    path('dashboard-teknisi/', views.dashboard_teknisi, name='dashboard_teknisi'),
    path('progress-teknisi/', views.progress_teknisi, name='dashboard_teknisi'),
    path('management-naker/', views.management_naker, name='management_naker'),
    path('add-naker/', views.add_naker, name='add_naker'),
    path('add-natura/', views.add_natura, name='add_natura'),
    path('add-nota/', views.add_nota, name='add_nota'),    
    path('add-posisi/', views.add_posisi, name='add_posisi'),  







    path('edit-sto/<int:id>/', views.sto_edit, name='sto_edit'),    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('check-db/', views.check_database_connection, name='check_database_connection'),
    path('sto-list/', views.sto_list, name='sto_list'),
    path('jenisnota-list/', views.jenisNota_list, name='jenisNota_list'),
    path('posisi-list/', views.posisi_list, name='posisi_list'),
    path('project/', views.project, name='project'),
    path('natura-list/', views.natura_list, name='natura_list'),
    path('kendaraan-list/', views.kendaraan_list, name='kendaraan_list'),
    path('bbm-list/', views.transaksiBBM_list, name='bbm_list')






    # path('forgot-password/', views.password_reset, name='forgot-password'),




]

