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
    path('get-naker-data/', views.get_naker_data, name='get_naker_data'), 
    path('add-project/', views.add_project, name='add_project'),
    path('add-sto/', views.add_sto, name='add_sto'), 
    path('finance/management/posisi-list/<int:pk>/', views.posisi_edit, name='posisi_edit'),



    path('finance/management/nota-list/<int:pk>/', views.nota_edit, name='nota_edit'),
    path('finance/management/sto-list/<int:pk>/', views.sto_edit, name='sto_edit'),
    # path('edit-sto/<int:id>/', views.sto_edit, name='sto_edit'),    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('check-db/', views.check_database_connection, name='check_database_connection'),
    path('sto-list/', views.sto_list, name='sto_list'),
    path('management-nota', views.jenisNota_list, name='nota_list'),
    path('posisi-list/', views.posisi_list, name='posisi_list'),
    path('project-list/', views.project_list, name='project_list'),
    path('natura-list/', views.natura_list, name='natura_list'),
    path('kendaraan-list/', views.kendaraan_list, name='kendaraan_list'),
    path('bbm-list/', views.transaksiBBM_list, name='bbm_list')






    # path('forgot-password/', views.password_reset, name='forgot-password'),




]

