from django import template
from productdb.models import Product

register=template.Library()

@register.simple_tag
def get_name(pk):
    x=Product.objects.get(productid=pk)
    return x.pname

@register.simple_tag
def get_price(pk):
    x=Product.objects.get(productid=pk)
    return x.price

@register.simple_tag
def get_url(pk):
    x=Product.objects.get(productid=pk)
    return x.url