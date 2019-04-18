from django import forms
from django.utils import timezone
from .models import Order


class OrderForm(forms.Form):
   name = forms.CharField(label='Атыңыз')
   last_name = forms.CharField(label='Фамилияңыз')
   phone = forms.CharField(label='Нөмеріңіз')
   buying_type = forms.ChoiceField(widget=forms.Select(), label='Алу жолы', choices=([('self', 'Самовывоз'), ('delivery', 'Доставка')]))
   address = forms.CharField(label='Адресіңіз', help_text='Адресіңізді міндетті түрде жазыңыз!', required=False)
   date = forms.DateField(widget=forms.SelectDateWidget(), label='Дата' ,initial=timezone.now())
   comment = forms.CharField(widget=forms.Textarea, label='Комментариіңіз', required=False)
