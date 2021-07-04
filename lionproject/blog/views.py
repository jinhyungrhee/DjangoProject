from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm
# Create your views here.


def home(request):
    blogs = Blog.objects.all() # home함수가 모든 블로그 객체를 보냄
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page') # .get()을 하면 정보가 오지 않아도 넘어감
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, id):
    # 객체를 가지고 오든지 404(Not Found error) 리턴
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})


def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid(): # 유효성 검사
        new_blog = form.save(commit=False) # 임시저장
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)  # 요청이 보내졌을 때 어떤 화면으로 이동할 것인지 리턴
    return redirect('home')

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})


def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()  # 빼먹으면 데이터베이스에 수정이 안됨!
    return redirect('detail', update_blog.id)


def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
