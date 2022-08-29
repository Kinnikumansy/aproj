from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),# created by uni
    #path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),# created by uni
    path('dashboard', views.dashboard, name="dashboard")# created by uni
]
