from django.urls import path
from.import views

urlpatterns = [
    path('dashboard-admin/', views.dashboard_admin, name='dashboard-admin'),
    path('management-bbm/', views.report_admin_bbm, name='management-bbm')
]

