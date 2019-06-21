from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse, HttpResponse
from .models import Country, Cart, CartItem, Order
from django.views.generic import View 
from decimal import Decimal
from .forms import OrderForm
from django.contrib import messages
import requests
import json
import pprint

def home(request):
   countries = Country.objects.filter(better=True)
   return render(request, 'TourfirmApp/index.html', context={'countries':countries})

class CountryDetail(View):
   def get(self, request, slug):
      try: 
         cart_id = request.session['cart_id']
         cart = Cart.objects.get(id=cart_id)
         request.session['total'] = cart.items.count()
      except:
         cart = Cart()
         cart.save()
         cart_id = cart.id
         request.session['cart_id'] = cart_id
         cart = Cart.objects.get(id=cart_id)
      turkey = Country.objects.get(id=1)
      spain = Country.objects.get(id=2)
      country = get_object_or_404(Country, slug__iexact=slug)
      r = requests.get(f'http://localhost:8000/api/shop/country/{country.slug}')
      pprint.pprint(r.json())
      return render(request, 'TourfirmApp/country_detail.html', context={
         'country': r.json(),
         'turkey': turkey,
         'spain': spain,
         'cart':cart,
      })


class ToursList(View):
   def get(self, request):
      try: 
         cart_id = request.session['cart_id']
         cart = Cart.objects.get(id=cart_id)
         request.session['total'] = cart.items.count()
      except:
         cart = Cart()
         cart.save()
         cart_id = cart.id
         request.session['cart_id'] = cart_id
         cart = Cart.objects.get(id=cart_id)
      r = requests.get('http://localhost:8000/api/shop/country/')
      return render(request, 'TourfirmApp/tours_list.html', context={'countries':r.json(), 'cart': cart,})


def cart_view(request):
   try: 
      cart_id = request.session['cart_id']
      cart = Cart.objects.get(id=cart_id)
      request.session['total'] = cart.items.count()
   except:
      cart = Cart()
      cart.save()
      cart_id = cart.id
      request.session['cart_id'] = cart_id
      cart = Cart.objects.get(id=cart_id)
   context = {
      'cart': cart,
   }
   return render(request, 'TourfirmApp/cart.html', context)


def add_to_cart_view(request):
   try: 
      cart_id = request.session['cart_id']
      cart = Cart.objects.get(id=cart_id)
      request.session['total'] = cart.items.count()
   except:
      cart = Cart()
      cart.save()
      cart_id = cart.id
      request.session['cart_id'] = cart_id
      cart = Cart.objects.get(id=cart_id)
   slug = request.GET.get('country_slug')
   cart.add_to_cart(slug)
   new_cart_total = 0.00
   for item in cart.items.all():
      new_cart_total += float(item.item_total)
   cart.cart_total = new_cart_total
   cart.save()
   return JsonResponse({'cart_total': cart.items.count(), 'cart_total_price': cart.cart_total})
   

def remove_from_cart_view(request):
   try: 
      cart_id = request.session['cart_id']
      cart = Cart.objects.get(id=cart_id)
      request.session['total'] = cart.items.count()
   except:
      cart = Cart()
      cart.save()
      cart_id = cart.id
      request.session['cart_id'] = cart_id
      cart = Cart.objects.get(id=cart_id)
   slug = request.GET.get('country_slug')
   cart.remove_from_cart(slug)
   new_cart_total = 0.00
   for item in cart.items.all():
      new_cart_total += float(item.item_total)
   cart.cart_total = new_cart_total
   cart.save()
   return JsonResponse({'cart_total': cart.items.count(), 'cart_total_price': cart.cart_total})


def change_item_qty(request):
   try: 
      cart_id = request.session['cart_id']
      cart = Cart.objects.get(id=cart_id)
      request.session['total'] = cart.items.count()
   except:
      cart = Cart()
      cart.save()
      cart_id = cart.id
      request.session['cart_id'] = cart_id
      cart = Cart.objects.get(id=cart_id)
   qty = request.GET.get('qty')
   item_id = request.GET.get('item_id')
   cart_item = CartItem.objects.get(id=int(item_id))
   cart.change_qty(cart_item, qty)
   return JsonResponse({
      'cart_total':cart.items.count(), 
      'item_total':cart_item.item_total,
      'cart_total_price': cart.cart_total,
   })


def checkout_view(request):
   try: 
      cart_id = request.session['cart_id']
      cart = Cart.objects.get(id=cart_id)
      request.session['total'] = cart.items.count()
   except:
      cart = Cart()
      cart.save()
      cart_id = cart.id
      request.session['cart_id'] = cart_id
      cart = Cart.objects.get(id=cart_id)
   context = {
      'cart':cart
   }

   return render(request, 'TourfirmApp/checkout.html', context)


def order_create_view(request):
   try: 
      cart_id = request.session['cart_id']
      cart = Cart.objects.get(id=cart_id)
      request.session['total'] = cart.items.count()
   except:
      cart = Cart()
      cart.save()
      cart_id = cart.id
      request.session['cart_id'] = cart_id
      cart = Cart.objects.get(id=cart_id)
   form = OrderForm()
   if request.method == 'POST':
      form = OrderForm(request.POST)
      if form.is_valid():
         data = {
            'items' : cart,
            'first_name' : form.cleaned_data['name'],
            'last_name' : form.cleaned_data['last_name'],
            'phone' : form.cleaned_data['phone'],
            'address' : form.cleaned_data['address'],
            'buying_type' : form.cleaned_data['buying_type'],
            'comment' : form.cleaned_data['comment'],
            'total' : cart.cart_total
         }
         print(data['buying_type'])
         r = requests.post('http://localhost:8000/api/shop/order/create/', data)
         print(r)
         print(r.json())
         del request.session['cart_id']
         del request.session['total']
         messages.success(request, f'Тапсырыс сәтті қабылданды! Қоңырауды күтіңіз')
         return render(request, 'TourfirmApp/order.html')
   context = {
      'form': form,
      'cart': cart,
   }
   return render(request, 'TourfirmApp/order.html', context)
