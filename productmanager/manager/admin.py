from django.contrib import admin
from .models import User, Product
#from . import models
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class productAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
    
admin.site.register(Product, productAdmin)

admin.site.register(User)