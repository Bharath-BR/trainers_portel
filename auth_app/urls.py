from django.urls import path
from . import views


urlpatterns=[
    path('register/',views.register_view,name='signup'),
    path('signin/',views.signin_view,name='signin'),
    path('signout/',views.signout_view,name='signout'),
]