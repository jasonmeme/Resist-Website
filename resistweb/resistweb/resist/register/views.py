from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate

from .forms import RegisterForm

# Create your views here.

def register(request):
	context = {}
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST['username']
			password = request.POST['password2']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			return redirect("/home")
	else:
		form = RegisterForm()
	context['form'] = form
	return render(request, "register/register.html", context)
