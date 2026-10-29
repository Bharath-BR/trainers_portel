from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserLoginForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('display')
    context={}
    if request.method=='POST':
        form=UserRegisterForm(data=request.POST)

        if form.is_valid():
            pwd1=form.cleaned_data['password']
            pwd2=form.cleaned_data['confirm_password']

            if pwd1==pwd2:
                user=form.save(commit=False)  #create ->create_user()

                user.set_password(pwd1)  #it encrypts the password
                user.save()

                login(request,user=user)
                return redirect('display')
            else:
                form.add_error('confirm_password','Password and Confirm Password Missmatch!')
    
    else:
        form=UserRegisterForm()

    context={
        'form':form,
        'operation':"Register",
    }

    return render(request,'register.html',context)

def signin_view(request):
    if request.user.is_authenticated:
            return redirect('display')

    context={}

    if request.method=="POST":
        form=UserLoginForm(data=request.POST)

        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user=user)
                return redirect('display')
            else:
                form.add_error('password','Inavalid Credentials')
    else:
        form=UserLoginForm()
    context={
        'form':form,
        'operation':'Login'
    }

    return render(request,'signin.html',context)


@login_required(login_url='signin')
def signout_view(request):
    if request.method=='POST':
          logout(request)
          return redirect('signin')

    return render(request,'signout.html')
