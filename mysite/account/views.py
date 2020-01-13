from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm, UserForm, ProfileForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User


# Create your views here.
def user_login(request):

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse("login successfully")
                else:
                    return HttpResponse("inactive Account")

            else:
                return HttpResponse("Invalid Login")

    else:
        login_form = LoginForm()

    return render(request, "account/login.html", {"form": login_form})


@login_required
def dashboard(request):
    return render(request, "account/dashboard.html", {'section': 'dashboard'})


def register(request):
    if request.method=="POST":
        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            cd = registration_form.cleaned_data
            new_user.set_password(cd['password2'])
            new_user.save()
            return render(request, "account/register_done.html", {'new_user': new_user})

    else:
        registration_form = RegistrationForm()

    return render(request, "account/register.html", {"user_form": registration_form})


@login_required
def edit(request):

    if request.method=="POST":
        user_form = UserForm(instance=request.user,
                             data=request.POST)
        profile_form = ProfileForm(instance=request.user.profile,
                                   data=request.POST,
                                   files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserForm(instance=request.user.profile)

    return render(request,'account/edit/html', {'user_form': user_form,
                                                'profile_form': profile_form})
