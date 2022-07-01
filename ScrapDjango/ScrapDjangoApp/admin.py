from django.contrib import admin
from .models import Annonce

# Register your models here.
admin.site.register(Annonce)

class AdminAnnonce(admin.ModelAdmin):
    list_display= ('title', 'photo', 'description', 'prix')