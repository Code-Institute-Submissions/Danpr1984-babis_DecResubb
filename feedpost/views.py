from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Post, CustomUser, ParentProfile, GuestProfile, Profile, Comment
from .forms import PostForm, RegisterForm, ParentForm, GuestForm, ChildForm, CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.mail import send_mail



class NewUser(CreateView):
    model = CustomUser
    template_name = 'home.html'
    form_class = RegisterForm


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

class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'profile.html'
    queryset = Post.objects.order_by('created_at')
    form_class = PostForm

    
    def get_form_kwargs(self):
        form_kwargs = super(AddPostView, self).get_form_kwargs()
        form_kwargs.update({"request": self.request})
        return form_kwargs

#class AddComment(CreateView):
 #   model = Comment
  #  template_name = 'comment.html'
   ##form_class = CommentForm

class AddComment(View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        context = {
            'post': post,
            'form': form,
        }

        return render(request, 'profile.html', context)

    def post(self, request, *args, **kwargs):
        pass

