from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

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
class CreateUserForm(forms.ModelForm):
  password1 = forms.CharField(required=True, label='Contraseña', widget=forms.PasswordInput(attrs={
      'placeholder': 'Contraseña',
      'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
    })
  )
      
  password2 = forms.CharField(required=True, label='Confirmar Contraseña', widget=forms.PasswordInput(attrs={
      'placeholder': 'Confirmar Contraseña',
      'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
    })
  )

  
  class Meta():
    model = UserProfile

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

      'first_name': forms.TextInput(attrs={
        'placeholder': 'Nombre',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),

      'last_name': forms.TextInput(attrs={
        'placeholder': 'Apellido',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),

      'email': forms.EmailInput(attrs={
        'placeholder': 'Correo',
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),

      'img_profile': forms.FileInput(attrs={
        'class': 'w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md mb-6'
      }),
    }