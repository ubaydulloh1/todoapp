from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('user-register', views.register_page, name='register'),
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),

    path('', views.home_page, name='home'),
]