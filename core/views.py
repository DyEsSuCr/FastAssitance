from django.shortcuts import render


def home(request):
  url_template = 'index.html'

  return render(request, url_template)