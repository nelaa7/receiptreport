from django.urls import path
from.import views

urlpatterns = [
    path('dashboard-admin/', views.dashboard_admin, name='dashboard-admin'),
    path('report-bbm/', views.report_admin_bbm, name='report-bbm'),
    # path('form-kendaraan/', views.form_kendaraan, name='form-kendaraan'),
    path('list-kendaraan/', views.list_kendaraan, name='list-kendaraan'),
    path('dashboard-teknisi/', views.dashboard_teknisi, name='dashboard-teknisi'),
    path('progress-teknisi/', views.progress_teknisi, name='dashboard-teknisi'),
    path('management-naker/', views.management_naker, name='management-naker'),
    path('add-naker/', views.add_naker, name='add-naker'),
    path('data-naker/', views.data_naker, name='data-naker'),









    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('check-db/', views.check_database_connection, name='check_database_connection'),
    path('sto-list/', views.sto_list, name='sto_list'),
    path('jenisnota-list/', views.jenisNota_list, name='jenisNota_list'),
    path('posisi-list/', views.posisi_list, name='posisi_list'),
    path('project/', views.project, name='project'),





    # path('forgot-password/', views.password_reset, name='forgot-password'),




]

