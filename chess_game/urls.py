"""chess_backend URL Configuration

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
from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls.static import static
from chess_engine.views import *
from chess_game.forms import AuthForm
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('chess_engine.urls')),
    path(r'', include('django.contrib.auth.urls')),
    path(r'^login/$', views.LoginView.as_view(template_name='chess_engine/login.html'), name="login"),
    path(r'^register/$', RegisterView.as_view(), name="register"),
    path(r'^profile/(?P<pk>[0-9]+)$', ProfileView.as_view(), name='profile'),
    path(r'^profile/(?P<pk>[0-9]+)/update_password$', ProfileUpdatePasswordView.as_view(), name='update-password'),
    path(r'^profile/(?P<pk>[0-9]+)/history/(?P<type>[a-z]+)$', ProfileShowRankingHistoryView.as_view(), name='show-history'),
    path(r'^profile/(?P<pk>[0-9]+)/load_data$', ProfileLoadData.as_view(), name='profile-load-data'),
    path(r'^profile/(?P<pk>[0-9]+)/(?P<update_type>[a-z]+)/(?P<key>[a-zA-Z0-9_]+)/(?P<value>[a-zA-Z0-9_ -]+)$',
        ProfileUpdateKeyView.as_view(), name='profile-update-key'),
    path(r'^logout/$', views.LogoutView.as_view(next_page='/%5Elogin/$?next=/'), name='logout'),
    path(r'^documentation/$', DocumentationView.as_view(), name='documentation')
]
