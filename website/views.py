from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.



def home(request):

	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		# Authenticate
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			messages.success(request, 'You have been Logged In!!')
			return redirect('home')
		else:
			messages.success(request, 'There was an Error Logging In!!')
			return redirect('home')

	context = {}
	return render(request, 'home.html', context)


def register_user(request):
	context = {}
	return render(request, 'register.html', context)




def logout_user(request):

	logout(request)
	messages.success(request, "You have been Logged out.....")
	return redirect('home')