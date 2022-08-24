from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('', views.NewUser.as_view(), name='register'),
    path('parent', views.AddParent.as_view(), name='parent'),
    path('add_child', views.AddChild.as_view(), name='add_child'),
    path('guest', views.AddGuest.as_view(), name='guest'),
    path('post_detail', views.PostList.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('edit_post/<int:pk>/', views.PostEditView.as_view(), name='edit_post'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('my_children', views.MyChildren.as_view(), name='my_children'),
]