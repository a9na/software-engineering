"""
URL configuration for lab4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from images.views import home, index, detail, create_comment, like, create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('images/', index, name='index'),
    path('images/<int:id>/', detail, name='detail'),
    path('images/create/', create, name="create-image"),
    path('images/<int:id>/comments/create/', 
         create_comment, name="create_comment"),
    path('images/<int:id>/like/', like, name="like-image"),
]
