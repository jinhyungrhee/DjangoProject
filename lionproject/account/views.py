from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm

# Create your views here.
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = authenticate(request= request, username= username, password= password)
      if user is not None:
        login(request, user)
    return redirect("home")
  else:
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
  logout(request)
  return redirect("home")

def register_view(request):
  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save() # form안에 적어주는 정보 외에 꼭 필요한 정보가 없기 때문에 commit넣지 않음
      login(request, user)
    return redirect('home')
  else:
    form = RegisterForm()
    return render(request, 'signup.html', {'form':form})
