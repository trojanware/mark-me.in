from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^attendance/', include('attendance.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),

	# Required to make static serving work
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^$','attendance.views.home',{}),
	(r'^home/$','attendance.views.home',{}),
	(r'^login/$','attendance.views.login',{}),
	(r'^processLogin/$','attendance.views.processLogin',{}),
	(r'^Signup/(?P<id_user>\d+)/$','attendance.views.newUser',{}),
	#(r'^stage1/$','attendance.views.stage1',{}),
	(r'^processStage1/$','attendance.views.stage1',{}),
	(r'^processStage2/$','attendance.views.stage2',{}),
	(r'^registerUser/$','attendance.views.addUser',{}),
	#(r'^getTT/$','attendance.views.echoTT',{}),
	(r'^checkUser/$','attendance.views.checkUser',{}),
	(r'^details/$','custag.views.returnData',{}),
	(r'^updateData/$','attendance.views.updateData',{}),
	(r'^getPercentage/$','attendance.views.getPercentage',{}),
	(r'^logout/$','attendance.views.logout',{}),
	(r'^fetchData/$','attendance.views.fetchData',{}),
)
