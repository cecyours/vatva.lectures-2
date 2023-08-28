from django.shortcuts import render,redirect
from .forms import UserSignUpForm,CreatePostForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def home(request):
    return render(request,'home.html')

def logoutx(request):
    logout(request)
    return redirect('home')

def user_dashboard(request):
    return render(request,'user_dashboard.html')

def add_post(request):
    post_form = CreatePostForm()
    if request.method =="POST":
        post_form = CreatePostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            print("data saved...")
            return redirect('home')

        else:
            print("error..cv.ds ",post_form.errors)
    return render(request,'newpost.html',{'post_form':post_form})

def loginx(request):

    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            print("login")
            return redirect('home')
        else:
            print("invalid")

    return render(request,'login.html')

def signup(request):

    userForm = UserSignUpForm()
    if request.method=="POST":
        userForm = UserSignUpForm(request.POST);
        if userForm.is_valid():
            userForm.save()
            # redirect to login screen
            return redirect('login-coder')
        print(userForm.errors)
    return render(request,'signup.html',{'userForm':userForm})