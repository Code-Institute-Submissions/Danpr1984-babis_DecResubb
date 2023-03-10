from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Post, ParentProfile, GuestProfile, Profile, Comment


class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["is_guest", "is_parent", "username", "email"]


class PostForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        label="Name your moment",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
    )

    content = forms.CharField(
        required=False,
        label="Tell us more about this moment",
        widget=forms.Textarea(
            attrs={
                "rows": 5,
                "width": "60%",
                "class": "form-control",
                "placeholder": "Share your experience",
            }
        ),
    )

    class Meta:
        model = Post
        fields = "__all__"
        exclude = (
            "author",
            "likes",
            "slug",
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(PostForm, self).save(commit=False)
        user = None
        if self.request:
            if hasattr(self.request, "user"):
                # Almacenar el usuario
                user = self.request.user
        if commit:
            # Almacenar el usuario en host
            obj.author = user
            obj.save()
        return obj


class ParentForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        fields = "__all__"
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(ParentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(ParentForm, self).save(commit=False)
        user = None
        if self.request:
            if hasattr(self.request, "user"):
                # Almacenar el usuario
                user = self.request.user
        if commit:
            # Almacenar el usuario en host
            obj.user = user
            obj.save()
        return obj


class GuestForm(forms.ModelForm):
    class Meta:
        model = GuestProfile
        fields = "__all__"


class ChildForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = (
            "user",
            "friends",
        )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(ChildForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        obj = super(ChildForm, self).save(commit=False)
        user = None
        if self.request:
            if hasattr(self.request, "user"):
                # Almacenar el usuario
                user = self.request.user
        if commit:
            # Almacenar el usuario en host
            obj.user = user
            obj.save()
        return obj


class CommentForm(forms.ModelForm):
    model = Comment
    text = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "width": "60%",
                "class": "form-control",
                "placeholder": "Post your comments",
            }
        ),
    )

    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("author",)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["post"].widget = forms.HiddenInput()
