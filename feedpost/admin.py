from django.contrib import admin
from .models import Post, Profile
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Profile)


