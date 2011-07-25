def getSubjects(timetable):
	cpy_timetable = timetable
	subs = []
	for day in timetable:
		del day['day']
		for sub in day.values():
			subs.append(sub)
	return subs	
