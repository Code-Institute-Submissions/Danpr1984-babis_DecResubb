from django.contrib import admin
from .models import Post, Profile
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from .forms import PostForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = PostForm

    fieldsets = (
        *UserAdmin.fieldsets,  
        (
            'User role',
            {
                'fields': (
                    'is_parent',
                    'is_guest'
                )
            }
        )
    )
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

admin.site.register(Profile)






