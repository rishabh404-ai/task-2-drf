from django.urls import path,include
from myuserapp.views import UserRegisterAPIView, UserRecordViewSet
from rest_framework import routers



router = routers.DefaultRouter() 
router.register('time-record', UserRecordViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('register/',UserRegisterAPIView.as_view(),name='register')
]