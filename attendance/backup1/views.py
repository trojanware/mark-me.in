from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.utils import simplejson

def home(request):
	return render_to_response(u'home.htm',{},context_instance = RequestContext( request ))

def login(request):
	return render_to_response(u'login.htm',{})

def processLogin(request,uname,passwrd):
	#uname = request.GET['uname']
	#passwrd = request.GET['password']
	user = authenticate(username=uname,password=passwrd)
	ans = {'accepted':uname}
	if user is not None:
		if user.is_active:
			login(user)
			#ans['accepted'] = uname
	json = simplejson.dumps(ans)			
	return HttpResponse(json,mimetype='application/json')		

