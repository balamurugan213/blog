"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views
# from django.contrib import admin

app_name = 'accounts'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'signup/', views.signup_view,name='signup'),
    path(r'login/', views.login_view,name='login'),
    path(r'logout/', views.logout_view,name='logout'),
    # re_path(r'(?P<slug>[\w-]+)/$', views.articleDetailpage, name="detail")

]

urlpatterns += staticfiles_urlpatterns()