from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
]