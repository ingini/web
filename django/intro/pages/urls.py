from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index), # flask의 @app.route에 해당한다.
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),
    path('nameage/<str:name>/<int:age>/', views.nameage),
    path('mulage/<int:age1>/<int:age2>/', views.mulage),
    path('dtl/', views.dtl),
    path('birthday/', views.birthday),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('lotto/', views.lotto),
    path('recommend/', views.recommend),
    path('article_new/', views.article_new),
    path('article_create/', views.article_create),
    path('static_example', views.static_example),
]
