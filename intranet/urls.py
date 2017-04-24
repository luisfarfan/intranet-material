"""intranet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='login.html')),
    url(r'^usuarios/$', TemplateView.as_view(template_name='pages/usuarios/usuarios.html')),
    url(r'^usuarios/edit/(?P<id_usuario>.+)/$', TemplateView.as_view(template_name='pages/usuarios/addedit.html')),
    url(r'^usuarios/add/$', TemplateView.as_view(template_name='pages/usuarios/addedit.html')),
    url(r'^proyectos/', TemplateView.as_view(template_name='pages/proyectos.html')),
    url(r'^sistemas/', TemplateView.as_view(template_name='pages/sistemas.html')),
    url(r'^permisos/', TemplateView.as_view(template_name='pages/permisos.html')),
    url(r'^roles/', TemplateView.as_view(template_name='pages/roles.html')),
]
