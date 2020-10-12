from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import UserRegister, UserRecord
from .serializers import UserRegisterSerializer, UserRecordSerializer
from rest_framework.exceptions import ValidationError
from .utils import Util
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response

class UserRegisterAPIView(generics.GenericAPIView):
    queryset = UserRegister.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self,request):

        serializer = self.serializer_class(request.data) 
        name       = request.data.get('name')
        idcard_no  = request.data.get('idcard_no')
        id_type    = request.data.get('id_type')
        address    = request.data.get('address')
        phone_no   = request.data.get('phone_no')
        email      = request.data.get('email')
        meet_with  = request.data.get('meet_with')

        if not name:
            raise ValidationError({'status':'failed',
                                   'message':'Name is required !',
                                   'data':[]})

        if not idcard_no:
            raise ValidationError({'status':'failed',
                                   'message':'Idcard No is required !',
                                   'data':[]})
                                   
        if not id_type:
            raise ValidationError({'status':'failed',
                                   'message':'Id_type is required !',
                                   'data':[]})

        if not address:
            raise ValidationError({'status':'failed',
                                   'message':'Address is required !',
                                   'data':[]})

        if not phone_no:
            raise ValidationError({'status':'failed',
                                   'message':'Phone No is required !',
                                   'data':[]})

        if not email:
            raise ValidationError({'status':'failed',
                                   'message':'Email is required !',
                                   'data':[]})
        
        if not meet_with:
            raise ValidationError({'status':'failed',
                                   'message':'Please enter the person you want to meet with !',
                                   'data':[]})                           
        


        # Email Config For New User     
        if email:
            email_body = 'Hello New User, Welcome to our office for the very first time.'
            data       = {'email_body': email_body, 'to_email': email, 'email_subject': 'Thank You'}    
            Util.send_mail(data)
  


        # Email Config For Existing User  
        if UserRegister.objects.filter(email=email).exists():

            user_email = UserRegister.objects.get(email=email)
            email_body = 'Hello User,Welcome Back Again.'
            data       = {'email_body': email_body, 'to_email': user_email.email, 'email_subject': 'Thank You'}    
            Util.send_mail(data)

        try :
            register = UserRegister.objects.create(
                                    name=name,idcard_no=idcard_no,id_type=id_type,address=address,phone_no=phone_no,email=email,meet_with=meet_with)

            register.save()     
            return Response({'status': 'success',
                             'message':'Thank you for your details !',
                             'data': serializer.data},status=status.HTTP_201_CREATED)        

        except:
            raise ValidationError({'status':'failed',
                                   'message':'Something went wrong. Please try again !',
                                   'data':[]})  

            
    



class UserRecordViewSet(viewsets.ModelViewSet):
    queryset = UserRecord.objects.all()
    serializer_class = UserRecordSerializer