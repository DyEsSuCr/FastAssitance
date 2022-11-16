from django.urls import path
from apps.accounts import views 

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/users/', views.get_users , name='users'),
    path('dashboard/create_user/', views.create_user , name='create_user'),
    path('dashboard/edit_user/', views.edit_user , name='edit_user'),
]