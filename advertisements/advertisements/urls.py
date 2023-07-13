"""
URL configuration for advertisements project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# Извините, я уже разобрался, как сделать сделать адрес  http://127.0.0.1/lesson_4. Т.к. вы еще не проверили задание, я изменил.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson_4', include('app_lesson_4.urls')),
]
