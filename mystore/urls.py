from django.contrib import admin
from django.urls import path
from django import urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from mystore import views

app_name = 'mystore'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product_detail/(\d+)/$', views.product_detail, name='product_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)