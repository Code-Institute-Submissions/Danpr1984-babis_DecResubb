from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View, DeleteView 
from .models import Post, CustomUser, ParentProfile, GuestProfile, Profile, Comment
from .forms import PostForm, RegisterForm, ParentForm, GuestForm
from .forms import ChildForm, CommentForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


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

    def get_form_kwargs(self):
        form_kwargs = super(AddChild, self).get_form_kwargs()
        form_kwargs.update({"request": self.request})
        return form_kwargs


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
   #template_name = 'profile.html'

    def get_context_data(self, **kwargs):

        context = super(AddPostView, self).get_context_data(**kwargs)
        context['postform'] = PostForm()
        return context

    def get_form_kwargs(self):
        form_kwargs = super(AddPostView, self).get_form_kwargs()
        form_kwargs.update({"request": self.request})
        return form_kwargs


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'profile.html'
    queryset = Post.objects.order_by('-created_at')
    form_class = PostForm, CommentForm

    def get_context_data(self, **kwargs):

        context = super(PostList, self).get_context_data(**kwargs)
        context['commentform'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = self.request.user
            obj.save()
            return redirect('profile')


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form = ['content', 'title', ]
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse_lazy('profile')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

#class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
 #   model = Post
  #  success_url = reverse_lazy('profile')

   # def test_func(self):
    #    post = self.get_object()
     #   return self.request.user == post.author
