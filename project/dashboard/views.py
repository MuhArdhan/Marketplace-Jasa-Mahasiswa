from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.urls import reverse
import json

from transactions.models import Transaction
from users.models import Vendor, Customer
from services.models import Jasa


# Create your views here.
def dashboard_admin_view(request):
    transactions_data = Transaction.objects.select_related(
        'customer_id_customer',
        'jasa_id_jasa',
        'jasa_id_jasa__vendor_id_vendor',
        'payment'
    ).all()
    
    list_jasa = Jasa.objects.all()
    list_vendor = Vendor.objects.annotate(jumlah_jasa=Count("jasa"))
    list_customer = Customer.objects.annotate(jumlah_transaksi=Count("transaction"))
    return render(request, 'dashboardadmin.html', {'transactions_data': transactions_data, 'list_jasa': list_jasa, 'list_vendor': list_vendor, 'list_customer': list_customer})

def update_listing_jasa(request):
    if request.method == 'POST':
        id_jasa = request.POST.get('id_jasa')
        name_jasa = request.POST.get('name_jasa')
        status = request.POST.get('status')
        harga = request.POST.get('harga')
        deskripsi = request.POST.get('deskripsi')

        try:
            jasa = Jasa.objects.get(id_jasa=id_jasa)
            jasa.name_jasa = name_jasa
            jasa.status = status
            jasa.harga = harga
            jasa.deskripsi = deskripsi
            jasa.save()
            
            base_url = reverse('dashboard_admin') 
            return redirect(f"{base_url}#listing-title")
        
        except Jasa.DoesNotExist:
            # Handle the case where the Jasa does not exist
            pass

    return dashboard_admin_view(request)

@require_POST
def update_status_jasa(request):
    try:
        data = json.loads(request.body)
        id_jasa = data.get('id')
        new_status = data.get('status') # 'Published', 'Unpublished'
        print("Received status update request:", data)
        print("Updating Jasa ID:", id_jasa, "to status:", new_status)
        jasa = get_object_or_404(Jasa, pk=id_jasa)
        jasa.status = new_status
        jasa.save()

        return JsonResponse({
            'success': True,
            'new_status': new_status,
            'message': f'Status jasa berhasil diubah menjadi {new_status}'
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

# --- 2. UPDATE STATUS USER ---
@require_POST
def update_status_user(request):
    try:
        data = json.loads(request.body)
        user_id = data.get('id')
        new_status = data.get('status') # 'Aktif', 'Diblokir'
        role = data.get('role')  # 'Customer' atau 'Vendor'
        is_delete = data.get('is_delete_action')   
        
        if role == 'Customer':
            target_model = Customer
        elif role == 'Vendor': # atau 'Seller'
            target_model = Vendor
        else:
            return JsonResponse({'success': False, 'message': 'Role tidak valid'}, status=400)
                
        user = get_object_or_404(target_model, pk=user_id)    
        
        # Update text status
        if is_delete:
            user.is_deleted = not user.is_deleted
        else:
            user.status = new_status
            user.is_deleted = False
            
        user.save()

        return JsonResponse({
            'success': True,
            'new_status': new_status,
            'is_deleted': user.is_deleted,
            'message': f'User berhasil diubah menjadi {new_status}'
        })
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)

def dashboard_seller_view(request):
    return render(request, 'dashboardseller.html')

def add_product_view(request):
    return render(request, 'add_product.html')

def edit_product_view(request):
    return render(request, 'edit_product.html')

