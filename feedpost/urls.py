from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='profile'),
    path('', views.HomeView.as_view(), name="login"),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
]