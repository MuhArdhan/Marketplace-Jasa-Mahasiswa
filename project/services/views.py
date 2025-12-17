from django.shortcuts import render
from .models import Jasa
from django.shortcuts import get_object_or_404

def shop(request):
    jasa_list = Jasa.objects.all()
    print(jasa_list)
    return render(request, "shop.html", {
        "jasa_list": jasa_list
    })

def product_page(request, id):
    jasa = get_object_or_404(Jasa, id_jasa=id)
    return render(request, "productpage.html", {
        "jasa": jasa
    })