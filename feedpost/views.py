from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Post
from cloudinary.models import CloudinaryField


class PostList(ListView):
    model = Post
    queryset = Post.objects.order_by('created_at')
    template_name = 'profile.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    #post to cloudinary
    fields = '__all__'


class HomeView(View):

    def get(self, request):
        return render(request, "home.html")

@login_required
def add_post(request):
    """
    A method to let users create a new blog post
    """
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'add_post.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(reverse('profile'))    
        else:
            print(form.errors)
            return render(request, 'add_post.html', {'form': form})