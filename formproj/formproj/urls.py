"""formproj URL Configuration

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
from . import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^frmexp/', include('frmexp.urls',namespace="frmexp")),
    #url(r'^accounts/signup/$', auth_views.signup, name='account_signup'),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/auth/$', auth_views.auth_view),
    url(r'^accounts/logout/$', auth_views.logout),
    url(r'^accounts/loggedin/$', auth_views.loggedin),
    url(r'^invalid/$', auth_views.invalid_login),
]
