from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.hashers import make_password
from .models import *
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def home(request):
    recherche = request.GET.get('search', '')
    users = User.objects.filter(username__icontains=recherche)
    return render(request, 'lerecap/coco/home.html', {'users': users, 'recherche': recherche})

def inscription(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User(username=username, password=make_password(password), email=email)
        user.save()
        login(request, user)
        content = render_to_string('lerecap/coco/email.html', {'user': user})
        send_mail('Bienvenue', '', 'marouaneindustries@mail.com', [user.email], html_message=content)
        return redirect('home')
    return render(request, 'lerecap/coco/inscription.html')

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'lerecap/coco/connexion.html')

def deco(request):
    logout(request)
    return redirect('home')

def passwordchange(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            send_mail('maj password', 'Ton mdp à été modifier', 'marouaneindustries@mail.com', [user.email])
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'lerecap/coco/passwordchange.html', {'form': form})

def homeadmin(request):
    return render(request, 'lerecap/coco/homeadmin.html')