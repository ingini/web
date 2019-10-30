from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'utils/index.html') # render는 모든 템플릿 폴더를 찾는다