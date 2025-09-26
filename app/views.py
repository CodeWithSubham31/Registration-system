from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
# Create your views here.
def home(request):
	if request.user.is_anonymous:
		return render(request,"signup.html")
	return render(request,"index.html")
	
	
def user_signup(request):
	if request.method=="POST":
		username=request.POST.get("username")
		email=request.POST.get("email")
		password=request.POST.get("password")
		if User.objects.filter(username=username).exists():
			#return HttpResponse("Username already exists")
			messages.error(request, "Username is not exists")
			return redirect("/user_signup")
		user = User.objects.create_user(username,email,password)
		if not username:
		          messages.error("Please fill the form") 
		          return render(request,"signup.html")
		user.save()
		return render(request,"signin.html")
	return render(request,"signup.html")
	

def user_signin(request):
	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return render(request,"index.html")
			
		elif not username:
		     messages.error("Please fill the form") 
		     return render(request,"signin.html")
		     
		else:
			messages.error(request,"invalid username or password")
			return render(request,"signin.html")
	return render(request,"signin.html")
def user_logout(request):
	logout(request)
	return render(request,"signin.html")