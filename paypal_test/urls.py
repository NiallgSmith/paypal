"""paypal_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views as home_views
from paypal_store import views as paypal_views
from paypal.standard.ipn import urls as paypal_urls
from products import views as product_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_views.get_index, name='index'),
    url(r'^paypal/', include(paypal_urls)),
    url(r'^paypal-return$', paypal_views.paypal_return),
    url(r'^paypal-cancel/$', paypal_views.paypal_cancel),
    url(r'^products/$', product_views.all_products),
]
