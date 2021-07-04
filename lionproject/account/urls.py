from django.urls import path
from .views import *  # blog 앱에 있는 views.py에 있는 모든 함수 가져옴

urlpatterns = [
  path('login/', login_view, name = "login"), 
  path('logout/', logout_view, name= "logout"),
  path('register/', register_view, name="signup"),
]