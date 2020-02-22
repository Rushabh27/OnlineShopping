from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views import generic
from django.template.context_processors import csrf
from productdb.models import Product
from django.contrib.auth.decorators import login_required

#@login_required(login_url='/loginmodule/login/')
def index(request):
	cat=request.POST.get('cat','')
	if cat!='':
		p1=Product.objects.filter(category=cat)
	else:
		p1=Product.objects.all()
	return render(request, 'index1.html', {'product1' : p1})

#@login_required(login_url='/loginmodule/login/')
def select(request):
	pid=request.POST.get('productid')
	print("hi",pid)
	p1=Product.objects.get(productid=pid)
	
	return render(request, 'iphonex1.html', {'product1': p1})

def search(request):
	inp=request.POST.get('search','')
	print(inp)
	p=Product.objects.filter(pname=inp)
	return render(request,'index1.html',{'product1':p})
# Create your views here.
