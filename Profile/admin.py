from django.contrib import admin
from .models import AuxCustomerProfileData, AuxMentorProfileData, AuxStudentProfileData, AuxProfileData

admin.site.register(AuxCustomerProfileData)
admin.site.register(AuxMentorProfileData)
admin.site.register(AuxStudentProfileData)
admin.site.register(AuxProfileData)
