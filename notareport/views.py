from django.shortcuts import render

# View Finance
def dashboard_admin(request):
    return render(request, 'finance/dashboard.html')

def report_admin_bbm(request):
    return render(request, 'finance/report/bbm.html')

def dashboard_teknisi(request):
    return render(request, 'teknisi/layouts/dashboard-teknisi.html')

def histori(request):
    return render(request, 'teknisi/layouts/dashboard-teknisi.html')