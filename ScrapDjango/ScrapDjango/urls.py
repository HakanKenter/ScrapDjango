"""ScrapDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ScrapDjangoApp.views import index, all_annonce, details_annonce, add_annonce, update_annonce, delete_annonce, confirmation, scraping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('all_annonce', all_annonce, name="all_annonce"),
    path('<int:id>/annonce', details_annonce, name="details_annonce"),
    path('add_annonce', add_annonce, name="add_annonce"),
    path("<int:id>/update_annonce", update_annonce, name="update_annonce"),
    path("<int:id>/delete_annonce", delete_annonce, name="delete_annonce"),
    path("confirmation", confirmation, name="confirmation"),
    path("scraping", scraping, name="scraping"),
]
