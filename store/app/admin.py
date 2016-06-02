from django.contrib import admin
from app.models import *
# Register your models here.

class iphoneadmin(admin.ModelAdmin):
    pass
admin.site.register(products, iphoneadmin)

admin.site.register(userprofiles, iphoneadmin)

admin.site.register(payments, iphoneadmin)

admin.site.register(comments, iphoneadmin)