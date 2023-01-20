from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.db import models



# Create your views here.

def cart_details(request, tot=0, count=0, ct_items=None):
    if request.user.id:
        try:
            ct = cartlist.objects.get(cart_id=c_id(request))
            ct_items = items.objects.filter(cart=ct, active=True,is_delete=False)
            for i in ct_items:
                tot += (i.products.price * i.quantity)
                count += i.quantity
        except ObjectDoesNotExist:
            pass
        return render(request, 'cartdetails.html', {'ci': ct_items, 't': tot, 'cn': count})
    return redirect('login')


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
        c_items = items.objects.get(user=request.user,products=prod, cart=ct)
        if c_items.quantity < c_items.products.stock:
            c_items.quantity += 1
        c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(user=request.user,products=prod, quantity=1, cart=ct)
        c_items.save()
    return redirect('cartdetails')


def min_cart(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(user=request.user,products=prod, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')


def delete_cart(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(user=request.user,products=prod, cart=ct)
    c_items.is_delete=True
    c_items.save()
    return redirect('cartdetails')


def delivery_details(request, amount=0, total=0):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        landmark = request.POST['landmark']
        city = request.POST['city']
        address_type = request.POST['address_type']
        print("name=", name)
        address = del_details.objects.create(name=name, number=number, landmark=landmark, city=city,
                                             address_type=address_type, username=request.user)
        address.save()
        # try:
        #     ct = cartlist.objects.get(cart_id=c_id(request))
        #     ct_items = items.objects.filter(cart=ct, active=True)
        #     for i in ct_items:
        #         total += (i.products.price * i.quantity)
        #         amount=total+5
        # except ObjectDoesNotExist:
        #     pass
        # addresses = del_details.objects.filter(username=request.user)
        return redirect('all_address')
    else:
        return render(request, 'delivery_details.html')


def payment(request):
    if request.method == 'POST':
        return render(request, 'order_successful.html')
    else:
        try:
            ct = cartlist.objects.get(cart_id=c_id(request))
            ct_items = items.objects.filter(cart=ct, active=True,is_delete=False)
            for i in ct_items:
                total += (i.products.price * i.quantity)
                amount = total + 5
        except ObjectDoesNotExist:
            pass
        return render(request, 'payment.html')


def order_successful(request):
    # if request.user.id:
    # delivery details
    # add=get_address(request)
    # print("address:",add)
    # user = del_details.objects.filter(username=request.user)
    # print('username =',user.get())
    obj = orders.objects.filter(username=request.user).latest('id')
    # obj = orders.objects.latest('id')
    # user details
    # user=User.objects.all().filter(username=request.user)
    # now=datetime.now()+timedelta(3)
    # dt=now.strftime('%d-%b-%Y')

    # try:
    #     ct = cartlist.objects.get(cart_id=c_id(request))
    #     ct_items = items.objects.filter(cart=ct, active=True)
    #     for i in ct_items:
    #         total += (i.products.price * i.quantity)
    #         amount=total+5
    # except ObjectDoesNotExist:
    #     pass
    
    item = ordered_items.objects.filter(order=obj)
    # items.objects.get(user=request.user).delete()
    amt=0
    for i in item:
        amt=i.amount
    return render(request, 'order_successful.html', {'obj': obj, 'item': item,"amt":amt})


# return redirect('login')


# def get_address(request):
#     # if request.user.id:
#         # add=del_details.objects.get(pk=request.POST['address_id'])

#         return add


def all_address(request, amount=0, total=0):
    if request.method == "POST":
        add = request.POST['address_id']
        # order_successful(request,add,amount,total)
        # print("all_address address:", add)
        # try:
        #     ct = cartlist.objects.get(cart_id=c_id(request))
        #     ct_items = items.objects.filter(cart=ct, active=True)
        #     for i in ct_items:
        #         total += (i.products.price * i.quantity)
        #         amount = total + 5
        # except ObjectDoesNotExist:
        #     pass
        address = del_details.objects.get(id=add)
        # prod=product.objects.filter(id=ct_items)
        name = address.name
        number = address.number
        landmark = address.landmark
        city = address.city
        address_type=address.address_type
        now = datetime.now() + timedelta(3)
        dt = now.strftime('%Y-%m-%d')
        #print('address=', address)
        user = request.user
        # print("ct=",ct)
        # print("ct_items=",ct_items)

        # for cart_item in ct_items:
        #     prod = cart_item.products.id
        #     product_instance = product.objects.get(id=prod)

        # pr=product.objects.get(id=ct_items_id)
        # print("product_instance=",product_instance)
        order = orders(username=user, name=name,number=number,landmark=landmark,city=city,address_type=address_type, delivery_date=dt)
        order.save()
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True,is_delete=False)
        amount=0
        for i in ct_items:
            print(
                "---------------------------------------------------------------------------------------------------------------")
            total += (i.products.price * i.quantity)
            amount = total + 5
            item = items.objects.get(id=i.id)
            order_item = ordered_items(order=order, product=item, quantity=i.quantity, price=i.products.price,amount=amount)
            order_item.save()
        return render(request, 'payment.html', {'order_item':order_item})
    else:
        addresses = del_details.objects.filter(username=request.user)
        return render(request, 'all_address.html', {'address': addresses})


# def order_product(request):
#     amount = 0
#     total = 0
#     try:
#         ct = cartlist.objects.get(cart_id=c_id(request))
#         ct_items = items.objects.filter(cart=ct, active=True)
#         for i in ct_items:
#             total += (i.products.price * i.quantity)
#             amount = total + 5
#     except ObjectDoesNotExist:
#         pass
#     return render(request, 'payment.html', {'amt': amount, 'tot': total})


class detailsdeleteview(DeleteView):
    model = del_details
    template_name = 'delete_details.html'
    success_url = reverse_lazy('all_address')


def all_orders(request):
    # print("current user=",user)
    # user = request.user
    # order = orders.objects.order_by('-id').first()
    order = orders.objects.filter(username=request.user).order_by('-id')
    # for i in order:
    #     ord=i.id
    # print("order=",ord)
    # # order_item = ordered_items.objects.filter(order=ord).order_by('-id')
    # order_item = ordered_items.objects.filter(order=ord)
    # amt=0
    # for i in order_item:
    #     amt=i.amount
    return render(request, 'orders.html', {'order':order})


def deliverd_items(request, id):
    print("-------------------------id : ", id)
    order = orders.objects.get(id=id)
    print("---------------------------------order : ", order)
    item = ordered_items.objects.filter(order=order)
    print("-----------------------------------------------: ", item)
    return render(request, 'ordered_items.html', {'order': item})