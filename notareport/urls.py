from django.urls import path
from.import views

urlpatterns = [
    path('dashboard-admin/', views.dashboard_admin, name='dashboard-admin'),
    path('report-bbm/', views.report_admin_bbm, name='report-bbm'),
    path('form-kendaraan/', views.form_kendaraan, name='form-kendaraan')

]

