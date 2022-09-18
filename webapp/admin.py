from django.contrib import admin
from webapp.models import Resume

# Register your models here.

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','mobile']