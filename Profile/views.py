from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from .models import AuxStudentProfileData, AuxCustomerProfileData, AuxMentorProfileData, AuxProfileData
from .serializers import ProfileSerializer


class AuxProfileDataView(APIView):
    def get(self, request):
        users = AuxProfileData.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response({"users": serializer.data})


class AuxStudentProfileDataView(APIView):
    def get(self, request):
        students = AuxStudentProfileData.objects.all()
        return Response({"students": students})


class AuxCustomerProfileDataView(APIView):
    def get(self, request):
        customers = AuxCustomerProfileData.objects.all()
        return Response({"customers": customers})


class AuxMentorProfileDataView(APIView):
    def get(self, request):
        mentors = AuxMentorProfileData.objects.all()
        return Response({"mentors": mentors})
