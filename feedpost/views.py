from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Post, CustomUser, ParentProfile, GuestProfile, Profile
from .forms import PostForm, RegisterForm, ParentForm, GuestForm, ChildForm
from django.core.mail import send_mail


class NewUser(CreateView):
    model = CustomUser
    template_name = 'home.html'
    form_class = RegisterForm

    #def check_user(request):
    
     #   if  request.user.id == is_guest:
       #     redirect("guest.html")

      #  elif request.user.id == is_parent:
            
       #     redirect("parent.html")

        #else:
         #   redirect("home.html")    


class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by('created_at')
    template_name = 'profile.html'
    form_class = PostForm

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm


class HomeView(CreateView):
    model = CustomUser
    template_name = 'home.html'
    form_class = RegisterForm

class AddParent(CreateView):
    model = ParentProfile
    template_name = 'parent.html'
    form_class = ParentForm

class AddGuest(CreateView):
    model = GuestProfile
    template_name = 'guest.html'
    form_class = GuestForm

class AddChild(CreateView):
    model = Profile
    template_name = 'add_child'
    form_class = ChildForm

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            [""]
        )
