from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime,timedelta
from django.contrib.auth.models import User

# Create your views here.

def cart_details(request, tot=0, count=0, ct_items=None):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.products.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cartdetails.html', {'ci': ct_items, 't': tot, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = product.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(products=prod, cart=ct)
        if c_items.quantity < c_items.products.stock:
            c_items.quantity += 1
        c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(products=prod, quantity=1, cart=ct)
        c_items.save()
    return redirect('cartdetails')


def min_cart(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(products=prod, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')


def delete_cart(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(products=prod, cart=ct)
    c_items.delete()
    return redirect('cartdetails')


def delivery_details(request,amount=0,total=0):
    if request.method=='POST':
        name=request.POST['name']
        number=request.POST['number']
        landmark=request.POST['landmark']
        city=request.POST['city']
        address_type=request.POST['address_type']
        address=del_details.objects.create(name=name, number=number, landmark=landmark,city=city,address_type=address_type,username=request.user)
        address.save()
        try:
            ct = cartlist.objects.get(cart_id=c_id(request))
            ct_items = items.objects.filter(cart=ct, active=True)
            for i in ct_items:
                total += (i.products.price * i.quantity)
                amount=total+5
        except ObjectDoesNotExist:
            pass
        return render(request, 'payment.html',{'amt':amount,'tot':total})
    else:
        return render(request, 'delivery_details.html')
    

def payment(request):
    return render(request, 'payment.html')


def order_successful(request,amount=0,total=0):
    obj=del_details.objects.all()
    user=User.objects.all()
    now=datetime.now()+timedelta(3)
    dt=now.strftime('%Y-%m-%d')
    
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            total += (i.products.price * i.quantity)
            amount=total+5
    except ObjectDoesNotExist:
        pass
    return render(request,'order_successful.html',{'obj':obj,'amt':amount,'tot':total,'date':dt,'user':user})

        