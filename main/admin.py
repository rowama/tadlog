from django.contrib import admin
from main.models import Tad

class TadAdmin(admin.ModelAdmin):
    fields=['note']

admin.site.register(Tad, TadAdmin)