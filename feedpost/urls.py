from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('profile', views.PostList.as_view(), name='profile'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
]