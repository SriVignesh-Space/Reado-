from django.urls import path,include
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name='index'),
    path("register/",views.register,name='register'),
    path("profile/",views.profile,name='profile'),
    path("login/",auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html') , name='logout'),
    path('addpost/',views.AddPost,name='addpost'),
    path('viewpost/<int:id>/',views.viewpost,name='viewpost'),
]