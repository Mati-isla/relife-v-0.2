from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login

def home(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")
def cuenta(request):
    return render(request,"cuenta.html")
def loginpage(request):
	if request.user.is_authenticated:
		return redirect(cuenta)
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect(cuenta)
			else:
				messages.info(request, 'Usuario y/o contraseña incorrecto')
		context = {}
		return render(request, "login.html", context) 





