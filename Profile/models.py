from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class AuxMentorProfileData(models.Model):
    pass


class AuxStudentProfileData(models.Model):
    pass


class AuxCustomerProfileData(models.Model):
    pass


class AuxProfileData(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='aux', on_delete=models.CASCADE)

    aux_admin = models.OneToOneField(AuxMentorProfileData, related_name='owner', on_delete=models.SET_NULL, null=True,
                                     blank=True)
    aux_student = models.OneToOneField(AuxStudentProfileData, related_name='owner', on_delete=models.SET_NULL,
                                       null=True, blank=True)
    aux_customer = models.OneToOneField(AuxCustomerProfileData, related_name='owner', on_delete=models.SET_NULL,
                                        null=True, blank=True)

    country = models.CharField('Country', null=True, blank=True, max_length=50)
    city = models.CharField('City', null=True, blank=True, max_length=50)
    telephone = PhoneNumberField('Telephone', null=True, blank=True, unique=True)
    age = models.IntegerField('Age', null=True, blank=True)
    rate = models.FloatField('Rate', null=True, blank=True)
