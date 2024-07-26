from django.urls import path
from .views import BlogView, HomeView

urlpatterns = [
    path('<int:pk>/<str:slug>/', BlogView.as_view(), name='blog_detail'),
    path('', HomeView.as_view(), name='blog_list'),
]