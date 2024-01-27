from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.



def home(request):

	records = Record.objects.all()


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

	context = {'records':records}
	return render(request, 'home.html', context)


def register_user(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, 'You have Successfully Registered')
			return redirect('home')

	form = SignUpForm()
	return render(request, 'register.html', {'form':form})



def logout_user(request):

	logout(request)
	messages.success(request, "You have been Logged out.....")
	return redirect('home')

def customer_record(request, pk):
	if request.user.is_authenticated:
		# lookup records

		customer_record = Record.objects.get(id=pk)
		return render(request, 'record.html', {'customer_record':customer_record})

	messages.success(request, 'You must be logged in to Visit this page')
	return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:

		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted")
		return redirect('home')
	messages.success(request, "You must be logged in to delete records")
	return redirect('home')


def add_record(request):

	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method =="POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added")
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})

	messages.success(request, "You must be logged in")
	return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form =AddRecordForm(request.POST or None, instance = current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Updated Successfully!!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	messages.success(request, "You must be logged")
	return redirect('home')

