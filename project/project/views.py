from django.shortcuts import render
from services.models import Jasa

def home(request):
    jasa_list = Jasa.objects.filter(status='Published').order_by('?')[:3]
    return render(request, 'home.html', {
        'jasa_list': jasa_list
    })