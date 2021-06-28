"""Quesko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.forms import forms
# re_path allows us to create path for our views based on regex
from django.urls import path, include, re_path
from users.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView
from core.views import IndexTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # used by django to login user
    path("accounts/", include("django.contrib.auth.urls")),

    # create new user via browser(package by django),by default RegistrationView uses django's User model but we modify it to use CustomUser model
    path("accounts/register/", RegistrationView.as_view(form_class=CustomUserForm,
         success_url='/'), name="django_registration_register"),

    path("accounts/", include("django_registration.backends.one_step.urls")),

    # Login Via browsable api
    path("api-auth/", include("rest_framework.urls")),

    path("api/", include("questions.api.urls")),

    path("api/", include("users.api.urls")),

    # Login via REST
    path("api/rest-auth/", include("rest_auth.urls")),

    # registration via REST
    path("api/rest-auth/registration/", include("rest_auth.registration.urls")),

    # redirects to login page
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
