from django.shortcuts import render

# Create your views here.
from .forms import CreateUserForm
def home(req):
    return render(req,'home.html')

def sign(req):

    userForm = CreateUserForm()
    if req.method =="POST":
        userForm = CreateUserForm(req.POST)
        if userForm.is_valid():
            userForm.save();
            print("data saved...")
        print("cdfjdshfjkbghj")
        print("errors",userForm.errors)
    return render(req,'signup.html',{'userForm':userForm})