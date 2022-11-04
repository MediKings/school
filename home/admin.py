from django.contrib import admin
from .models import Universite, Faculte, Departement, Promotion


admin.site.register(Universite)
admin.site.register(Faculte)
admin.site.register(Departement)
admin.site.register(Promotion)
