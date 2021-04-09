from django.urls import path

from .views import AuxStudentProfileDataView, AuxMentorProfileDataView, AuxCustomerProfileDataView, AuxProfileDataView

urlpatterns = [
    path('students/', AuxStudentProfileDataView.as_view()),
    path('mentors/', AuxMentorProfileDataView.as_view()),
    path('customers/', AuxCustomerProfileDataView.as_view()),
    path('profiles/', AuxProfileDataView.as_view()),
]