from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Post

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = Profile
        fields = ['image']


class PostForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.Textarea()
    # category = forms.ModelChoiceField(queryset=Category.objects.all())
    image = forms.ImageField()

    class Meta:
        model = Post
        fields = ['title','content','category','image']