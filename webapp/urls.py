"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from portfolio.views import *
from accounts.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('portfolio/',portfolio,name='portfolio'),
    path('details/',details,name='details'),
    path('delete_details/<id>/',delete_details,name='delete_details'),      #here the url will pass the id argument that means its a dynamic url
    path('update_details/<id>/',update_details,name='update_details'),      #here the url will pass the id argument that means its a dynamic url
    #path('search_details',search_details,name='search_details'),
    path('register/',register,name='register'),
    path('login_page/',login_page,name='login_page'),
    path('apply/',apply,name = 'apply'),
    path('dashboard/',dashboard,name='dashboard'),
    path('test/',test,name='test'),
    path('exam/',exam,name='exam'),
    path('marks/',marks,name='marks'),
    path('student_login/',student_login,name='student_login')
]
