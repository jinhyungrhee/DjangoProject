#from django.contrib import admin # 필요없음
from django.urls import path
from .views import *  # blog 앱에 있는 views.py에 있는 모든 함수 가져옴

urlpatterns = [
    # path('admin/', admin.site.urls), # home과 admin은 필요없음!
    #path('', home, name='home'),
    path('<str:id>', detail, name='detail'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('edit/<str:id>', edit, name='edit'),
    path('update/<str:id>', update, name='update'),
    path('delete/<str:id>', delete, name='delete'),
]
