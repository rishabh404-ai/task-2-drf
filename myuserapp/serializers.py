from rest_framework import serializers
from .models import UserRegister, UserRecord


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRegister
        fields = '__all__'




class UserRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRecord
        fields = '__all__'

