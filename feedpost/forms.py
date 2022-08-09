from django import forms
from .models import CustomUser, Post, ParentProfile, GuestProfile, Profile
from django.contrib.auth.forms import UserCreationForm
#class RegistrationForm(forms.ModelForm):


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ["is_guest", "is_parent", "username", "password1", "email"]

class PostForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        label="Name your moment",
        widget=forms.TextInput(attrs={
            "class": "form-control",
        })
    )

    content = forms.CharField(
        required=False,
        label="Tell us more about this moment",
        widget=forms.Textarea(attrs={
            'rows': 6,
            'width':'60%',
            'class': 'form-control',
            'placeholder': 'Share your experience'}))
    
    class Meta:
        model = Post
        fields = '__all__'
            
class ParentForm(forms.ModelForm):   

    class Meta:
        model = ParentProfile
        fields = '__all__'

class GuestForm(forms.ModelForm):   

    class Meta:
        model = GuestProfile
        fields = '__all__'

class ChildForm(forms.ModelForm):   

    class Meta:
        model = Profile
        fields = '__all__'