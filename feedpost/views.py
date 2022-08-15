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
    
    def get_form_kwargs(self):
        form_kwargs = super(AddPostView, self).get_form_kwargs()
        form_kwargs.update({"request": self.request})
        return form_kwargs


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

class AddComment(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'social/post_detail.html', context)
        
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = post
            new_comment.save()

        comments = Comment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'profile', context)
#class AddComment(CreateView):
 #   model = Comment
  #  template_name = 'profile'
   # queryset = Comment.objects.order_by('created_on')
    #form_class = CommentForm