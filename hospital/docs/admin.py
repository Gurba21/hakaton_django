from django.contrib import admin
from .models import *


# class HospAdmin(admin.ModelAdmin):
#     list_display = ('hosp_okpo', 'hosp_region', 'hosp_name', 'hosp_number', 'hosp_maindoc',
#                     'hosp_docs', 'hosp_nurses', 'hosp_patients', 'hosp_gos',)
#     search_fields = ('hosp_name', 'hosp_region')
#     list_filter = ('hosp_name', 'hosp_region')
#     list_display_links = ('hosp_name',)
#     save_on_top = True
#
# class HospAdmin(admin.ModelAdmin):
#     list_display = ('hosp_okpo', 'hosp_region', 'hosp_name', 'hosp_number', 'hosp_maindoc',
#                     'hosp_docs', 'hosp_nurses', 'hosp_patients', 'hosp_gos',)
#     search_fields = ('hosp_name', 'hosp_region')
#     list_filter = ('hosp_name', 'hosp_region')
#     list_display_links = ('hosp_name',)
#     save_on_top = True
#




admin.site.register(Hosp)
admin.site.register(Maindoctor)
admin.site.register(Nurses)
admin.site.register(Patients)
admin.site.register(Doctors)
# Register your models here.