from django.contrib import admin
from core.models import Todo
from core.models import Profile
# from attendance.models import Attendance
# Register your models here.
admin.site.register(Todo)
admin.site.register(Profile)
# admin.site.register(Attendance)