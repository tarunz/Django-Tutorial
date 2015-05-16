from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import UserProfile 
from django.template import RequestContext
from django.contrib.auth import authenticate, login

logged = False
username = ""

def index(request):
	global logged
	return render(request, 'login/index.html', {'conf':logged})

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        #    if 'picture' in request.FILES:
        #        profile.picture = request.FILES['picture']
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.web= request.POST['web']
        user.save();
    return render_to_response('login/register.html',{ 'registered': registered},context)

def signin(request):
	global logged, username 
	context = RequestContext(request)
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				logged = True
				return HttpResponseRedirect('/login/')
			else:
				return HttpResponse("Your account isn't activated yet :(")
		else:
			HttpResponse("Incorrect credentials \n")
	else:
		return render_to_response('login/signin.html', {}, context)

def renew(request):
    global username
    if request.method=='POST':
	   if request.POST['newpass1']== request.POST['newpass2']:
            nmail= request.POST['newmail']
            passw= request.POST['oldpass']
            passn= request.POST['newpass1']
            nweb = request.POST['newweb']
            if passn!=None:
                u = User.objects.get(username='username')
                u.set_password(passn)
                u.save()
            if nmail!=None:
                u = User.objects.get(username=username)
                u.email = nmail
                u.save()
            if nweb!=None:
                u = User.objects.get(username=username)
                u.web = nweb;
                u.save()
    return HttpResponseRedirect('/login/')
