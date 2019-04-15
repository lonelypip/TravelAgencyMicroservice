from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import JsonResponse, HttpResponse
from .models import Country, Cart, CartItem, Order
from django.views.generic import View 
from decimal import Decimal
from .forms import OrderForm
from django.contrib import messages



def home(request):
   countries = Country.objects.all()
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
      return render(request, 'TourfirmApp/country_detail.html', context={
         'country': country,
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
      countries = Country.objects.all()
      return render(request, 'TourfirmApp/tours_list.html', context={'countries':countries, 'cart': cart,})


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
         new_order = Order()
         new_order.user = request.user
         new_order.first_name = form.cleaned_data['name']
         new_order.last_name = form.cleaned_data['last_name']
         new_order.phone = form.cleaned_data['phone']
         if form.cleaned_data['address']:
            new_order.address = form.cleaned_data['address']
         else:
            new_order.address = ''
         new_order.buying_type = form.cleaned_data['buying_type']
         if form.cleaned_data['comments']:
            new_order.comments = form.cleaned_data['comments']
         else:
            new_order.comments = ''
         new_order.total = cart.cart_total
         new_order.save()
         del request.session['cart_id']
         del request.session['total']
         messages.success(request, f'Ваш комментарий успешно добавлен')
         return render(request, 'TourfirmApp/order.html')
   context = {
      'form': form
   }
   return render(request, 'TourfirmApp/order.html', context)
