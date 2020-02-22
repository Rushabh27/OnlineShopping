from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.views import generic
from django.template.context_processors import csrf
from .models import Order
from cartdb.models import Cart
from productdb.models import Product
from registration.models import Userdata
import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import smtplib
from django.core.mail import send_mail
from django.conf import settings 


@login_required(login_url='/loginmodule/login/')
def placeorder(request):
	request.session['id']=None
	if request.POST.get("id") is not None:
		request.session['id']=request.POST.get("id")
		print("hiiii",request.POST.get("id"))
	c={}
	c.update(csrf(request))
	
	return render(request,'billinginfo.html', )

@login_required(login_url='/loginmodule/login/')	
def addorderdetail(request):
	name =request.POST.get('name','')
	mobileno = request.POST.get('mo.no.','')
	area = request.POST.get('area','')
	landmark = request.POST.get('landmark','')
	buldingname = request.POST.get('bname','')
	city = request.POST.get('city','')
	state = request.POST.get('state','')
	pincode = request.POST.get('pincode','')
	add =[]
	add.append(name)
	add.append(mobileno)
	add.append(area)
	add.append(buldingname)
	add.append(landmark)
	add.append(city)
	add.append(state)
	add.append(pincode)
	print("hii")
	request.session['address']=add
	userid=request.session.get('userid')
	if request.session["id"] is not None :
		pid=request.session["id"]
		print('hi',pid)
		product = Product.objects.get(productid=pid)
		print("hi",product.price)
		tp=0
		tp+=product.price
		dd=datetime.date.today() + datetime.timedelta(days=7)
		return render(request,'orderinfo.html' ,{'address':add ,'product1':product,'tprice':tp,'ddate':dd})
	else:
		cart = Cart.objects.filter(username=userid)
		pid=[]
		for p in cart:
			pid.append(p.productid)
		print(pid)
		product = Product.objects.filter(productid__in=pid)
		tp=0
		for pr in product:
			tp+=pr.price
		dd=datetime.date.today() + datetime.timedelta(days=7)
		return render(request,'orderinfo.html' ,{'address':add , 'cart1':cart,'product1':product,'tprice':tp,'ddate':dd})

@login_required(login_url='/loginmodule/login/')
def ordersuccess(request):
	add=request.session['address']

	dd=datetime.date.today() + datetime.timedelta(days=7)
	ordertime=datetime.datetime.now()
	userid=request.session.get('userid')
	name=add[0]
	mobileno=add[1]
	area=add[2]
	buldingname=add[3]
	landmark=add[4]
	city=add[5]
	state=add[6]
	pincode=add[7]
	if request.session['id'] :
		pid=request.session['id']
		product = Product.objects.get(productid=pid)
		tp=0
		tp+=product.price
		o=Order(userid=userid,name=name,mobileno=mobileno,area=area,buldingname=buldingname,landmark=landmark,city=city,state=state,pincode=pincode,productid=pid,ddate=dd)
		o.save()
		list=[]
		list.append(landmark)
		subject="hijdhsk"
		message="hfgsk"
		"""email_from = settings.EMAIL_HOST_USER
		send_mail( subject, message, email_from, list)"""
		request.session['id']=None
		return render(request,'ordersuccess.html',{'ddate':dd,'address':add,'product1':product,'tprice':tp})

	else:
	
		cart = Cart.objects.filter(username=userid)
		pid=[]
		for p in cart:
			pid.append(p.productid)
		product = Product.objects.filter(productid__in=pid)
		tp=0
		for pr in product:
			tp+=pr.price
		for p in cart:
			o=Order(userid=userid,name=name,mobileno=mobileno,area=area,buldingname=buldingname,landmark=landmark,city=city,state=state,pincode=pincode,productid=p.productid,ddate=dd)
			o.save()
			
			# subject="hijdhsk"
			# message="hfgsk"
			# email_from = settings.EMAIL_HOST_USER
			# send_mail( subject, message, email_from, landmark)
	
		o1=Cart.objects.filter(productid__in=pid).delete()
		return render(request,'ordersuccess.html',{'ddate':dd,'address':add,'cart1':cart,'product1':product,'tprice':tp})
		
 
@login_required(login_url='/loginmodule/login/')
def vieworder(request):
	userid=request.session.get('userid')
	print(userid)
	o=Order.objects.filter(userid=userid)
	print(o)
	td=datetime.date.today()
	return render(request,'myorder.html',{'ord':o,'today':td})
	# return HttpResponse("hiiiii teri ma ki chu")


@login_required(login_url='/loginmodule/login/')
def orderdetail(request):
	userid=request.session.get('userid')
	return render_to_response('order_list.html',{'order1' : o , 'userid' : request.session.get('userid')} )

class OrderListView(generic.ListView):
	template_name='order_list.html'
	model = Order