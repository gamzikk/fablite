from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from .forms import RegisterForm, LoginForm, ProfileForm
from .models import Profile, CustomUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			login(request, new_user)
			return redirect('profile', new_user.id)
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form})


def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(email=cd['email'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('profile', user.id)
				else:
					return HttpResponse('Отключённая учётная запись')
			else:
				return HttpResponse('Неверный логин или пароль.')
	else:
		form = LoginForm()
	return render(request, 'users/login.html', {'form': form})


def user_logout(request):
	logout(request)
	return redirect('login')


@login_required
def profile(request, pk):
	profile = Profile.objects.get(pk=pk)
	return render(request, 'users/profile.html', {'profile': profile})


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()


def list_user(request):
	users = CustomUser.objects.all()
	return render(request, 'users/list_user.html', {'users': users})