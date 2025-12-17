from django.shortcuts import redirect, render
from users.models import Vendor
from .models import Jasa
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

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
    
def dashboard_seller(request):
    id = request.session.get('user_id')

    if not id:
        return redirect('login')

    vendor = Vendor.objects.get(id_vendor=id)
    jasa_list = Jasa.objects.filter(vendor_id_vendor=vendor)

    return render(request, 'dashboardseller.html', {
        'jasa_list': jasa_list
    })
    
def add_jasa(request):
    vendor_id = request.session.get("user_id")
    if not vendor_id:
        return redirect("login")

    vendor = Vendor.objects.get(id_vendor=vendor_id)

    if request.method == "POST":
        name_jasa = request.POST.get("name_jasa")
        deskripsi = request.POST.get("deskripsi")
        image = request.FILES.get("image")

        Jasa.objects.create(
            vendor_id_vendor=vendor,
            name_jasa=name_jasa,
            deskripsi=deskripsi,
            image=image
        )

        return redirect("dashboard_seller")

    return render(request, "addproduct.html")

def update_jasa(request, jasa_id):
    vendor_id = request.session.get("user_id")
    if not vendor_id:
        return redirect("login")

    jasa = get_object_or_404(
        Jasa,
        id_jasa=jasa_id,
        vendor_id_vendor__id_vendor=vendor_id
    )

    if request.method == "POST":
        jasa.name_jasa = request.POST.get("name_jasa")
        jasa.deskripsi = request.POST.get("deskripsi")
        jasa.image = request.FILES.get("image", jasa.image)
        jasa.save()

        return redirect("dashboard_seller")

    return render(request, "editproduct.html", {
        "jasa": jasa
    })
    
def delete_jasa(request, jasa_id):
    vendor_id = request.session.get("user_id")
    if not vendor_id:
        return redirect("login")

    jasa = get_object_or_404(
        Jasa,
        id_jasa=jasa_id,
        vendor_id_vendor__id_vendor=vendor_id
    )

    jasa.delete()
    return redirect("dashboard_seller")