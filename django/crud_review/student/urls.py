from django.urls import path
from . import views

urlpatterns = [
    # create
    path('new/', views.new),
    path('create/', views.create),
    # read
    path('', views.index),
    path('<int:pk>/', views.detail),
    # delete
    path('<int:pk>/delete/', views.delete),
    # update
    path('<int:pk>/edit/', views.edit),
    path('<int:pk>/update/', views.update),
]