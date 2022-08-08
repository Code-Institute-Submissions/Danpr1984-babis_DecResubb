from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Post, CustomUser
from .forms import PostForm, RegisterForm


class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by('created_at')
    template_name = 'profile.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm

class NewUser(CreateView):
    model = CustomUser
    template_name = 'register.html'
    form_class = RegisterForm

class HomeView(View):

    def get(self, request):
        return render(request, "home.html")

