from django.contrib import admin
from .models  import Sto, Posisi, Project, Unit, JenisNota, Naker,Kendaraan, Natura, TransaksiBBM, TransaksiNonBBM, MyUser

# Register your models here.
admin.site.register(Sto)
admin.site.register(Posisi)
admin.site.register(Project)
admin.site.register(Unit)
admin.site.register(JenisNota)

admin.site.register(Naker)
admin.site.register(MyUser)
admin.site.register(Kendaraan)
admin.site.register(TransaksiBBM)
admin.site.register(TransaksiNonBBM)



