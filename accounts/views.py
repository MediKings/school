from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()

def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username):
            messages.warning(request, "Ce nom d'utilisateur existe déjà")
            return redirect('accounts:register')
        else:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            if user:
                auth = authenticate(username=user.username, password=password)
                if auth is not None:
                    login(request, auth)
                    return redirect('accounts:login')
    return render(request, 'accounts/register.html', {})


def Login(request):
    username_email = request.POST.get('username_email')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(username=username_email).exists()):
            user = authenticate(username=username_email, password=password)
        elif(User.objects.filter(email=username_email).exists()):
            user = User.objects.get(email=username_email)
            user = authenticate(username=user.username, password=password)
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('accounts:login')
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Mot de passe incorrects! Réessayez")
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


def Logout(request):
    logout(request)
    return redirect('accounts:login')


@login_required
def ProfileView(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'accounts/profile.html', {'user': user})


@login_required
def UpdateProfile(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return HttpResponseRedirect(reverse('profile', args=[pk]))
    else:
        u_form = UserUpdateForm(request.POST, instance=user)
    return render(request, 'accounts/update_profile.html', {'u_form': u_form, 'profile': profile})
    