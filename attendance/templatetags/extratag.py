from django import template
register = template.Library()

@register.filter(name='div')
def div(lst):
	oprs = [int(arg) for arg in lst.split(',')]
	ans = oprs[0]/oprs[1]
	return ans
#div.is_safe = False
