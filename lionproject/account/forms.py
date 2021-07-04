from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm): # custom user에 맞는 회원가입 폼 생성
  class Meta:
    model = CustomUser
    fields = ['username', 'password1', 'password2', 'nickname', 'location', 'university']
