from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_post')
    #profile = models.ForeignKey(Child, on_delete=models.CASCADE, related_name="child_profile")
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    media = CloudinaryField('media', default='placeholder')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)
    likes = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_likes')

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['created_at']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()    


class Comment(models.Model):
    comment_sender = models.ForeignKey(User, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now_add=True)
    deleted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.pk   

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)     


class Profile(models.Model):
    child_name = models.CharField(max_length=200, unique=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    child_image = CloudinaryField('image', default='placeholder') 
    birthdate = models.DateField()
        
    def __str__(self):
        return self.title        