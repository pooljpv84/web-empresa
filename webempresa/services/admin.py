from django.contrib import admin
from .models import Service


# Register your models here.

# mostrar campos de fecha para lectura
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service,ServiceAdmin)