from django.contrib import admin
from .models import Student, MyUser, Track

# Register your models here.
admin.site.register(Student)
admin.site.register(MyUser)
admin.site.register(Track)