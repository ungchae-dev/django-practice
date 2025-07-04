"""
URL configuration for bc_community project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bcuser.views import home

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('bcuser/', include('bcuser.urls')), # bcuser로 요청이 오면 bcuser.urls에서 처리
    path('board/', include('board.urls')), 
    path('',home)
]
