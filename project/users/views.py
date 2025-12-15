from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import Admin, Vendor, Customer
from django.contrib.auth.hashers import make_password, check_password

def register_customer(request):
    if request.method == "POST":
        nama = request.POST["nama"]
        email = request.POST["email"]
        no_hp = request.POST["no_hp"]
        password = request.POST["password"]
        confirm = request.POST["confirm_password"]
        
        # Refill context
        context = {
            "nama": nama,
            "email": email,
            "no_hp": no_hp
        }

        if not nama or not email:
            messages.error(request, "Semua field wajib diisi")
            return render(request, "register_customer.html", context)

        if password != confirm:
            messages.error(request, "Password tidak sama")
            return render(request, "register_customer.html", context)

        if len(password) < 8:
            messages.error(request, "Password minimal 8 karakter")
            return render(request, "register_customer.html", context)

        if Customer.objects.filter(email=email).exists():
            messages.error(request, "Email sudah terdaftar")
            return render(request, "register_customer.html", context)      

        Customer.objects.create(
            nama=nama,
            email=email,
            no_hp=no_hp,
            password=make_password(password)
        )

        messages.success(request, "Registrasi berhasil, silakan login")
        return redirect("login")

    return render(request, "register_customer.html")

def register_vendor(request):
    if request.method == "POST":
        nama = request.POST["nama"]
        email = request.POST["email"]
        no_hp = request.POST["no_hp"]
        password = request.POST["password"]
        confirm = request.POST["confirm_password"]
        
        # Refill context
        context = {
            "nama": nama,
            "email": email,
            "no_hp": no_hp
        }


        if password != confirm:
            messages.error(request, "Password tidak sama")
            return render(request, "register_vendor.html", context)

        if Vendor.objects.filter(email=email).exists():
            messages.error(request, "Email sudah terdaftar")
            return render(request, "register_vendor.html", context)

        Vendor.objects.create(
            nama=nama,
            email=email,
            no_hp=no_hp,
            password=make_password(password)
        )

        messages.success(request, "Registrasi vendor berhasil")
        return redirect("login")

    return render(request, "register_vendor.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        # Refill context
        context = {
            "email": email
        }

        if not email or not password:
            messages.error(request, "Email dan password wajib diisi")
            return render(request, "login.html", context)

        # Admin
        admin = Admin.objects.filter(email=email).first()
        if admin and password == admin.password:
            request.session["role"] = "admin"
            request.session["user_id"] = admin.id_admin
            return redirect("dashboard_admin")
        
        # Vendor
        vendor = Vendor.objects.filter(email=email).first()
        if vendor and check_password(password, vendor.password):
            request.session["role"] = "vendor"
            request.session["user_id"] = vendor.id_vendor
            return redirect("dashboard_seller")

        # Customer
        customer = Customer.objects.filter(email=email).first()
        if customer and check_password(password, customer.password):
            request.session["role"] = "customer"
            request.session["user_id"] = customer.idcustomer
            return redirect("home")

        messages.error(request, "Email atau password salah")
        return render(request, "login.html", context)

    return render(request, "login.html")

def logout_view(request):
    request.session.flush()
    return redirect("login")

def vendor_dashboard(request):
    if request.session.get("role") != "vendor":
        return redirect("login")

    vendor_id = request.session.get("user_id")
    vendor = Vendor.objects.get(id_vendor=vendor_id)

    return render(request, "vendor/dashboard.html", {"vendor": vendor})
