from django.urls import path
from accounts.views import *
from . import views

app_name = "accounts"

urlpatterns = [
    path('login', views.login_view,name='login'),
    # path('logout', views.logout_view,name='logout'),
    path('signup', views.signup_view,name='signup'),
]