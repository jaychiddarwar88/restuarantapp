from django.contrib import admin
from .models import subs, pasta, salads, dinplatter, toppings, regularpizza, silicanpizza, cart, orders

# Register your models here.


admin.site.register(subs)
admin.site.register(pasta)
admin.site.register(salads)
admin.site.register(dinplatter)
admin.site.register(toppings)
admin.site.register(regularpizza)
admin.site.register(silicanpizza)
admin.site.register(cart)
admin.site.register(orders)
