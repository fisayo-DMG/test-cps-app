from django.contrib import admin
from .models import Student, Payment, Report

# Register your models here.
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(Report)