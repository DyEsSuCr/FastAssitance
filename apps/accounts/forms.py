from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, EmployeeProfile

class SigninForm(forms.ModelForm):
  class Meta:
    model = UserProfile

    fields = ('username', 'password')

    help_texts = {
      'username': None,
      'password': None,
    }

    widgets = {
      'username': forms.TextInput(attrs={
        'placeholder': 'Nombre de usuario',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),
      
      'password': forms.PasswordInput(attrs={
        'placeholder': 'Contraseña',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),
    }

# terminal
class CreateEmployeeForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    password1 = forms.CharField(required=True, label='Contraseña', widget=forms.PasswordInput(), help_text=('Just Enter the same password, for confirmation'))
    password2 = forms.CharField(required=True, label='Confirmar Contraseña', widget=forms.PasswordInput(), help_text=('Just Enter the same password, for confirmation'))

    model = EmployeeProfile

    fields = 'username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'img_profile'

    help_texts = {
      'username': None,
      'password1': None,
      'password2': None,
    }

    widgets = {
      'username': forms.TextInput(attrs={
        'placeholder': 'Nombre de usuario',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),
      
      'password1': forms.PasswordInput(attrs={
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),

      'password2': forms.PasswordInput(attrs={
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),

      'first_name': forms.TextInput(attrs={
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),

      'last_name': forms.TextInput(attrs={
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),

      'email': forms.EmailInput(attrs={
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),

      'img_profile': forms.FileInput(attrs={
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),
    }