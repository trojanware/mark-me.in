from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.utils import simplejson
from manager.models import tbl_Temp_Signup
from manager.models import Subject
from manager.models import Timetable
from django.contrib.auth.models import User
from UtilFunctions import getSubjects
from BTree import *
import datetime
import redis

def home(request):
	return render_to_response(u'home.htm',{},context_instance = RequestContext( request ))

def login(request):
	return render_to_response(u'login.htm',{})

def processLogin(request):
	uname = request.GET['uname']
	passwrd = request.GET['password']
	user = authenticate(username=uname,password=passwrd)
	ans = {'accepted':'False'}
	if user is not None:
		if user.is_active:
			login(user)
			ans['accepted'] = 'True'
			request.session['auth'] = 'True'
			request.session['id'] = uname
			request.session.set_expiry(0)
	json = simplejson.dumps(ans)			
	return HttpResponse(json,mimetype='application/json')		

def newUser(request,id_user):
	return render_to_response(u'AddUserInfo.htm',{"id_user":id_user})

def stage1(request):
	ans = {}
	user = request.GET['uname']
	passw = request.GET['pass']
	fname1 = request.GET['fname']
	lname1 = request.GET['lname']	
	
	try:
		u = User.objects.get(username=user)
	except:		
		temp_user = tbl_Temp_Signup(username=user,passwrd=passw,fname=fname1,lname=lname1,timestamp=datetime.datetime.now())
		temp_user.save()
		cur = tbl_Temp_Signup.objects.filter(username=user)
		if cur is not None:
			maxuser = cur[0]
			now = datetime.datetime.now()
			for temp in cur:
				if temp.timestamp > maxuser.timestamp:
					maxuser = temp
			userid = maxuser.id
			ans['id'] = userid
		ans['status'] = "Success"
	json = simplejson.dumps(ans)
	return HttpResponse(json,mimetype='application/json')

def stage2(request):
	college = request.GET['college']	
	branch = request.GET['branch']
	sem = request.GET['sem']
	section = request.GET['sec']
	usn = reuqest.GET['usn']

def addUser(request):
	coll = request.GET['coll']
	branch = request.GET['branch']
	sec = request.GET['sec']
	sem = request.GET['sem']
	usn = request.GET['usn']
	id_user = request.GET['id']
	tti = request.GET['tt']
	timetable = simplejson.loads(tti)
	cptimetable = []
	for r in timetable:
		cptimetable.append(r.copy())
	size = len(timetable)
	user = tbl_Temp_Signup.objects.get(id=id_user)
	username = user.username
	passwrd = user.passwrd
	fname = user.fname
	lname = user.lname
	new_user = User.objects.create_user(username,"",passwrd)
	new_user.fname = fname
	new_user.lname = lname
	new_user.save()
	add_info = new_user.get_profile()
	add_info.college = coll
	add_info.branch = branch
	add_info.section = sec
	add_info.semester = sem
	add_info.usn = usn
	add_info.save()

	subjects = getTT(timetable)	
	for subject in subjects:
		objSubject = Subject(user=new_user,name=subject)
		objSubject.save()
	dayIndex = {'Mon':0,'Tue':1,'Wed':2,'Thu':3,'Fri':4,'Sat':5,'Sun':6}
	frq = {}
	for sub1 in subjects:
		frq[sub1] = [0,0,0,0,0,0,0]
	for s in subjects:
		for day in cptimetable:
			ans = {'user':day['day']}
			if day.values().__contains__(s):
				count = 0
				for key,value in day.items():
					if value==s:
						count = count + 1
						if count == 1:
							frq[s].insert(dayIndex[day['day']],key[4:5])
						else:
							prevIndex = frq[s].__getitem__(dayIndex[day['day']])
							frq[s].__delitem__(dayIndex[day['day']])
							newIndex = prevIndex + ',' + key[4:5]
							frq[s].insert(dayIndex[day['day']],newIndex)
			else:				
				frq[s].insert(dayIndex[day['day']],0)	
	for su in subjects:
		subj=Subject.objects.get(user=new_user,name=su)	
		ar = frq[su]		
		tbl = Timetable(subject=subj,user=new_user,mon=ar[0],tue=ar[1],wed=ar[2],thu=ar[3],fri=ar[4],sat=ar[5],sun=ar[6])
		tbl.save()
	
	rep = simplejson.dumps(ans)
	return HttpResponse(rep,mimetype='application/json')

def getTT(timetable):
	ans = {}					
	subs = getSubjects(timetable)
	tree = Tree()
	fin_subs = tree.getSubjectList(subs)	
	i = 1
	for subject in fin_subs:
		strKey = 'hour'+str(i)
		ans[strKey] = subject
		i = i+1
	ans['noSubjects'] = len(fin_subs)
	return fin_subs		

def checkUser(request):
	reply={'reply':'no'}
	try:
		uname = request.session['id']
	except: pass
	if uname is not None:
		reply['reply'] = 'yes'
	json = simplejson.dumps(reply)
	return HttpResponse(json,mimetype="application/json")

def returnData(request):	
	#TODO: moved to custag
	try:
		userid = request.session['id']
	except: return render_to_response(u'home.htm',{})
	userl = User.objects.get(username=userid)
	subjects = Subject.objects.filter(user=userl)
	timetable = []
	dayIndex = ['mon','tue','wed','thu','fri','sat','sun']
	curr_day = datetime.datetime.now().weekday()
	day = dayIndex[curr_day]
	tt = {}
	for subj in subjects:
		t=Timetable.objects.get(subject=subj,user=userl)
		timetable.append(t)		
		if day == 'mon':
			tt[str(t.subject.name)] = int(t.mon)
		elif day == 'tue':
			tt[str(t.subject.name)] = int(t.tue)
		elif day == 'wed':
			tt[str(t.subject.name)] = int(t.wed)
		elif day == 'thu':
			tt[str(t.subject.name)] = int(t.thu)
		elif day == 'fri':
			tt[str(t.subject.name)] = int(t.fri)
		elif day == 'sat':
			tt[str(t.subject.name)] = int(t.sat)
		elif day == 'sun':
			tt[str(t.subject.name)] = int(t.sun)
	return render_to_response(u'Details.htm',{'Subjects':subjects,'user':userl,'tt':timetable,'day':curr_day,'dd':tt})

def updateData(request):
	user = request.GET['user']
	day = request.GET['day']
	subjectname = request.GET['subject']
	present = request.GET['checked']
	
	userl = User.objects.get(username=user)
	objsubject = Subject.objects.get(name=subjectname,user=userl)
	orgpresent = objsubject.getNoPresent()
	orgabsent = objsubject.getAbsent()
	orgtotal = objsubject.getTotal()
	if present == 'pre':
		orgpresent = orgpresent + 1
	elif present == 'let':
		orgtotal = orgtotal - 1
	else:
		orgabsent = orgabsent + 1
	orgtotal = orgtotal + 1
	percent = (orgpresent/orgtotal)*100
	objsubject = Subject.objects.filter(name=subjectname,user=userl).update(present=int(orgpresent),absent=int(orgabsent),totaldays=int(orgtotal),percentage=percent)
	ans = {'percent':percent,'absent':orgabsent,'total':orgtotal,'subject':subjectname,'present':orgpresent,'user':user}
	json = simplejson.dumps(ans)
	return HttpResponse(json,mimetype='application/json')

def getPercentage(request):
	try:
		user = request.GET['user']
		userl = User.objects.get(username=user)	
		objsubject = Subject.objects.filter(user=userl)
		nos = len(objsubject)
		dictSubject = {}
		lstSubjects = []
		for i in range(0,nos):
			dictSubject = {}
			dictSubject['name'] = objsubject[i].name
			dictSubject['present'] = objsubject[i].present
			dictSubject['total'] = objsubject[i].totaldays
			lstSubjects.append(dictSubject)
		json = simplejson.dumps(lstSubjects)
	except: pass
	return HttpResponse(json,mimetype='application/json')

def logout(request):
	del request.session['id']
	return HttpResponse("")

def fetchData(request):
	user = request.GET['user']
	names = request.GET['name']
	userl = User.objects.get(username=user)
	subj = Subject.objects.filter(user=userl,name=names)
	ans = {'total':subj[0].getTotal(),'present':subj[0].getNoPresent(),'absent':subj[0].getAbsent()}
	json = simplejson.dumps(ans)
	return HttpResponse(json,mimetype='application/json')
	
