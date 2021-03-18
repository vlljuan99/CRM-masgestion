from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

from CRM.models import Clientes, Comerciales

class ClientesResource(resources.ModelResource):
    class Meta:
        model = Clientes
        include = ('nombre')
        import_id_fields = ['DNI']

@admin.register(Clientes)
class ClientesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','nombre','DNI')
    resource_class = ClientesResource

@admin.register(Comerciales)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')