from django.conf.urls import url
from onlineshoppingapp import views
urlpatterns = [
	url(r'^index', views.index),
	url(r'^select', views.select),
        url(r'^iphonex1', views.select),
	url(r'^search',views.search),
]
