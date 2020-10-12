from django.urls import path,include
from myuserapp.views import UserRegisterViewSet, UserRecordViewSet
from rest_framework import routers



router = routers.DefaultRouter() 
router.register('register',UserRegisterViewSet)
router.register('time-record', UserRecordViewSet)



urlpatterns = [
    path('', include(router.urls)),
    #path('register/',RegisterView.as_view()),
    #path('entry/',RecordEntryView.as_view())
]