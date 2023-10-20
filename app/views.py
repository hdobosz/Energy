from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.views.generic.base import TemplateView # new


# Create your views here.
class HomePageView(TemplateView):
    template_name = "base.html" #new

def register(request):
    if request.method == 'POST':               # if form is submitted
        form = RegistrationForm(request.POST)  # create form
        if form.is_valid():                    # if form data is valid
            user = form.save(commit=False)     # create user, but don't save to database yet
            password = form.cleaned_data['password']  # get password from form
            user.set_password(password)               # set password
            user.save()                               # save user
            messages.success(request, 'Account created successfully')  # send success message
            # login(request, user)                      # login user
            return redirect('login')                   # redirect to home
    else:                                             # if form is not submitted
        form = RegistrationForm() # create form
    return render(request, 'users/register.html', {'form': form}) # render template


def user_login(request):
    if request.method == 'POST':        # if form is submitted
        form = LoginForm(request.POST)  # create form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)   # authenticate user
            if user is not None:           # if user exists
                login(request, user)   # login user
                return redirect('home')  # redirect to home
            else:
                form.add_error(None, f'Failed to authenticate user: {username}')
    else:                                # if form is not submitted
        form = LoginForm()               # create form
    return render(request, 'users/login.html', {'form': form})  # render template


def user_logout(request):
    logout(request)  # logout user
    return redirect('home')  # redirect to home





