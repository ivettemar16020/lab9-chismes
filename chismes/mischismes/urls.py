from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListChisme.as_view()),
    path('<int:pk>/', views.DetailChisme.as_view()),
]
