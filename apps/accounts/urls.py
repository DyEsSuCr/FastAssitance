from django.urls import path
from apps.accounts import views 

urlpatterns = [
    path('signin/', views.Signin.as_view(), name='signin'),
]