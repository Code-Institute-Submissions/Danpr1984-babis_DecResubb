from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('parent', views.AddParent.as_view(), name='parent'),
    path('add_child', views.AddChild.as_view(), name='add_child'),
    path('guest', views.AddGuest.as_view(), name='guest'),
    path('profile', views.PostList.as_view(), name='profile'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('edit_post/<int:pk>/', views.PostEditView.as_view(), name='edit_post'),
   # path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('', views.NewUser.as_view(), name='register'),
   
]