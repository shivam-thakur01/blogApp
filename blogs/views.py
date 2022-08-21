from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Post,Category

# Create your views here.
def home(request):
    posts=Post.objects.all()[0:]
    cat=Category.objects.all()
    data={'posts':posts,'cats':cat}
    return render(request,'index.html',data)

def post(request,url):
    cat=Category.objects.all()
    posts=Post.objects.get(url=url)
    data={'posts':posts,'cats':cat}
    return render(request,'post.html',data)

def category(request,url):
    print(url)
    cat=Category.objects.get(url=url)
    cat_name=Category.objects.all()
    posts=Post.objects.filter(cat=cat)
    data={'cats':cat_name,'category':cat,'posts':posts}
    return render(request,'category.html',data)