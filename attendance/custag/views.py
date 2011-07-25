from django.contrib.auth.models import User
from manager.models import Subject, Timetable
from django.shortcuts import render_to_response
import datetime

def returnData(request):
	#userid = ""
	try:
		userid = request.session['id']
	except: return render_to_response(u'home.htm',{})
	userl = User.objects.get(username=userid)
	subjects = Subject.objects.filter(user=userl)
	timetable = []
	dayIndex = ["mon",'tue','wed','thu','fri','sat','sun']
	curr_day = datetime.datetime.now().weekday()
	day = dayIndex[curr_day]
	tt = {}
	for subj in subjects:
		t=Timetable.objects.get(subject=subj,user=userl)
		timetable.append(t)		
		if day == 'mon':
			count = 0
			try:
				tt[str(t.subject.name)] = int(t.mon)
			except:
				nos = len(t.mon.split(','))
				for h in t.mon.split(','):
					count = count + 1
					name = str(t.subject.name)
					for i in range(1,count):
						name = name + ' '
					tt[name] = int(h)
		elif day == 'tue':
			count = 0
			try:
				tt[str(t.subject.name)] = int(t.tue)
			except:
				nos = len(t.tue.split(','))
				for h in t.tue.split(','):
					count = count + 1
					name = str(t.subject.name)
					for i in range(1,count):
						name = name + ' '
					tt[name] = int(h)
		elif day == 'wed':
			count = 0
			try:
				tt[str(t.subject.name)] = int(t.wed)
			except:
				nos = len(t.wed.split(','))
				for h in t.wed.split(','):
					count = count + 1
					name = str(t.subject.name)
					for i in range(1,count):
						name = name + ' '
					tt[name] = int(h)
		elif day == 'thu':
			count = 0
			try:
				tt[str(t.subject.name)] = int(t.thu)
			except:
				nos = len(t.thu.split(','))
				for h in t.thu.split(','):
					count = count + 1
					name = str(t.subject.name)
					for i in range(1,count):
						name = name + ' '
					tt[name] = int(h)
		elif day == 'fri':
			count = 0
			try:
				tt[str(t.subject.name)] = int(t.fri)
			except:
				nos = len(t.fri.split(','))
				for h in t.fri.split(','):
					count = count + 1
					name = str(t.subject.name)
					for i in range(1,count):
						name = name + ' '
					tt[name] = int(h)
		elif day == 'sat':
			count = 0
			try:
				tt[str(t.subject.name)] = int(t.sat)
			except:
				nos = len(t.sat.split(','))
				for h in t.sat.split(','):
					count = count + 1
					name = str(t.subject.name)
					for i in range(1,count):
						name = name + ' '
					tt[name] = int(h)
		elif day == 'sun':
			count = 0
			try:
				tt[str(t.subject.name)] = int(t.sun)
			except:
				nos = len(t.sun.split(','))
				for h in t.sun.split(','):
					count = count + 1
					name = str(t.subject.name)
					for i in range(1,count):
						name = name + ' '
					tt[name] = int(h)
	return render_to_response(u'Details.htm',{'Subjects':subjects,'user':userl,'tt':timetable,'day':curr_day,'dd':tt})
