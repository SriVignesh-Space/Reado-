from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Category
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PostForm

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-date')
    recent = Post.objects.order_by('-date')[:3]
    return render(request, 'index.html',{'posts':posts, 'recent':recent, 'categories':Category.objects.all()})



def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully! You can now login as {username}')
            return redirect('login')

    return render(request, 'register.html',{'form':form})

@login_required
def profile(request):
    # u_form = UserUpdateForm()
    # p_form = ProfileUpdateForm()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
    }
    return render(request, 'profile.html',context)

@login_required
def AddPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            author = request.user
            image = form.cleaned_data.get('image')
            category = form.cleaned_data.get('category')
            Post.objects.create(title=title,content=content,author=author,image=image,category=category)
            messages.success(request, f'Post added successfully!')
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'addpost.html',{'form':form})

def viewpost(request,id):
    post = Post.objects.get(id = id)
    return render(request, 'viewpost.html',{'post':post})