from django.shortcuts import render
from rest_framework import viewsets
from .models import UserRegister, UserRecord
from .serializers import UserRegisterSerializer, UserRecordSerializer


class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = UserRegister.objects.all()
    serializer_class = UserRegisterSerializer
    



class UserRecordViewSet(viewsets.ModelViewSet):
    queryset = UserRecord.objects.all()
    serializer_class = UserRecordSerializer