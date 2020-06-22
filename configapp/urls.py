"""configapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from core.views import (
    UserViewSet,
    UserCreate,
    Configuration
)

router = DefaultRouter()
router.register(r'users',UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/token/', obtain_auth_token, name='api-token'),
    url(r'api/', include(router.urls)),
    url(r'user/create/',UserCreate.as_view()),
    url(r'configs/list/',Configuration.as_view())
]
