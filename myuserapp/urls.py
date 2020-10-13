from django.urls import path,include
from myuserapp.views import UserRegisterAPIView, UserRecordAPIView



urlpatterns = [

    path('register/',UserRegisterAPIView.as_view(),name='register'),
    path('time-record/',UserRecordAPIView.as_view(),name='time-record')
    
]