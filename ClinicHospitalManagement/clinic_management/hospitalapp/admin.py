from django.contrib import admin

from hospitalapp.models import Department, Doctor, Appointment, Admin

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Admin)
