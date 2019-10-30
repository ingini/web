from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all().order_by('-id')

    context = {
        'articles' : articles,
    }
    return render(request, 'student/index.html', context)

def new(request):
    return render(request, 'student/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article.objects.create(title=title, content=content)

    return redirect(f'/student/{article.pk}/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'student/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/student/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'student/edit.html', context)

def update(request, pk):

    article = Article.objects.get(pk=pk)

    title = request.POST.get('title')
    content = request.POST.get('content')

    article.title = title
    article.content = content
    article.save()

    return redirect(f'/student/{article.pk}/')