from django.db import models
from django.shortcuts import reverse
from decimal import Decimal
from django.conf import settings
import requests
import json
# Create your models here.


class Country(models.Model):
   name = models.CharField(max_length=20)
   slug = models.SlugField()
   author = models.CharField(max_length=20)
   description = models.TextField()
   price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
   main_image = models.ImageField(upload_to='main/')
   background_image = models.ImageField(upload_to='background_images/', blank=True)
   image_1 = models.ImageField(upload_to='images/', blank=True)
   image_2 = models.ImageField(upload_to='images/', blank=True)
   image_3 = models.ImageField(upload_to='images/', blank=True)
   image_4 = models.ImageField(upload_to='images/', blank=True)
   sities = models.CharField(max_length=100)
   better = models.BooleanField(default=False)
   
   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('country_detail_url', kwargs={'slug': self.slug})


class CartItem(models.Model):
   country = models.ForeignKey(Country, on_delete=models.CASCADE)
   qty = models.PositiveIntegerField(default=1)
   item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

   def __str__(self):
      return "Cart item #{0}".format(self.id)


class Cart(models.Model):
   items = models.ManyToManyField(CartItem, blank=True)
   cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

   def __str__(self):
      return str(self.id)

   def add_to_cart(self, slug):
      cart = self
      country = Country.objects.get(slug=slug)
      new_item, _ = CartItem.objects.get_or_create(country=country, item_total=country.price)
      if new_item not in cart.items.all():
         cart.items.add(new_item)
         cart.save()

   def remove_from_cart(self, slug):
      cart = self
      country = Country.objects.get(slug=slug)
      for cart_item in cart.items.all():
         if cart_item.country == country:
            cart.items.remove(cart_item)
            cart.save()

   def change_qty(self, cart_item, qty):
      cart = self
      cart_item.qty = int(qty)
      cart_item.item_total = int(qty) * Decimal(cart_item.country.price)
      cart_item.save()
      new_cart_total = 0.00
      for item in cart.items.all():
         new_cart_total += float(item.item_total)
      cart.cart_total = new_cart_total
      cart.save()


ORDER_STATUS_CHOICES = {
   ('Принят в обработку', 'Принят в обработку'),
   ('Выполняется', 'Выполняется'),
   ('Оплачен', 'Оплачен')
}


class Order(models.Model):
   items = models.OneToOneField(Cart, on_delete=models.CASCADE, verbose_name='Корзина #')
   total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
   first_name = models.CharField(max_length=150)
   last_name = models.CharField(max_length=150)
   phone = models.CharField(max_length=30)
   address = models.CharField(max_length=255, blank=True)
   buying_type = models.CharField(max_length=40, choices=(('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')), default="Самовывоз", blank=True)
   date = models.DateTimeField(auto_now_add=True)
   comment = models.TextField(blank=True)
   status = models.CharField(max_length=100, choices=ORDER_STATUS_CHOICES)

   def __str__(self):
      return "Заказ №{0}".format(str(self.id))

   