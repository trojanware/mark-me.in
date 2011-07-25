from django import template
register = template.Library()

@register.filter(name='div')
def div(lst):
	oprs = [int(arg) for arg in lst.split(',')]
	ans = oprs[0]/oprs[1]
	return ans
#div.is_safe = False

@register.filter
def split(str,splitter):
    return str.split(splitter)

@register.filter
def sortVals(lst):
	vals = lst.items()
	for i in range(0,len(vals)):
   		for j in range(0,len(vals)-1):
			if vals[j].__getitem__(1)>vals[j+1].__getitem__(1):
				temp = vals[j]
				vals[j] = vals[j+1]
				vals[j+1] = temp
	return vals

