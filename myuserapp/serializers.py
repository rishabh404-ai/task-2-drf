from rest_framework import serializers
from .models import UserRegister, UserRecord


class UserRegisterSerializer(serializers.ModelSerializer):
    
    name      = serializers.CharField(required=True)
    idcard_no = serializers.IntegerField(required=True)
    id_type   = serializers.CharField(required=True)
    address   = serializers.CharField(required=True)
    phone_no  = serializers.CharField(required=True)
    email     = serializers.EmailField(required=True)
    meet_with = serializers.CharField(required=True)


    class Meta:
        model = UserRegister
        fields = ['name','idcard_no','id_type','address','phone_no','email','meet_with']




class UserRecordSerializer(serializers.ModelSerializer):

    name       = serializers.CharField(required=True)
    entry_time = serializers.CharField(required=True)
    exit_time  = serializers.CharField(required=True)


    class Meta:
        model = UserRecord
        fields = ['person','entry_time','exit_time']

