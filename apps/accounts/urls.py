from django.urls import path
from apps.accounts import views 

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/barbers/', views.get_users , name='barbers'),
    path('dashboard/edit_user/', views.edit_user , name='edit_user'),
]