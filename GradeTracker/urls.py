from django.conf.urls import patterns, url

from GradeTracker import views

urlpatterns = patterns('',

    url(r'^$', views.welcome, name='welcome'),
    url(r'^index', views.index, name='index'),

    url(r'^(?P<student_id>)/$', views.detail, name='detail'),
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<student_id>\d+)/account$', views.account, name='account'),
    url(r'^(?P<student_id>\d+)/accountedit$', views.editAccount, name='ediAccount'),

    #About us
    url(r'^about/$', views.about, name='about'),

    #Forgot password
    url(r'^forgot/$', views.forgot, name='forgot'),
    url(r'^validEmail/$', views.validEmail, name='validEmail'),

    #Course pages 
    url(r'^(?P<student_id>\d+)/(?P<course_id>\d+)/$', views.grades, name='grades'),
    url(r'^deleteCourse/(?P<course_id>\d+)/$', views.deleteCourse, name='delete-course'),
    url(r'^editcourse/(?P<course_id>\d+)/$', views.editCourse, name='edit-course'),

    #Activity Modification
    url(r'^(?P<student_id>\d+)/(?P<course_id>\d+)/(?P<graded_activity_id>\d+)$', views.addSub, name='activity'),
    url(r'^editactivity/(?P<activity_id>\d+)/$', views.editGradedActivity, name='edit-activity'),
    url(r'^deleteactivity/(?P<activity_id>\d+)/$', views.deleteGradedActivity, name='edit-activity'),

    #SubActivitity Modification
    url(r'^editsubactivity/(?P<subactivity_id>\d+)/$', views.editSubGradedActivity, name='edit-activity'),
    url(r'^deletesubactivity/(?P<subactivity_id>\d+)/$', views.deleteSubGradedActivity, name='edit-activity'),    

    #What-If Page
    url(r'^whatIf/(?P<student_id>\d+)/(?P<course_id>\d+)/$', views.whatIfView, name="whatIfView"),

    url(r'^(?P<student_id>\d+)/test/$', views.test, name='test'),

    #Templating System
    url(r'^searchtemplate/$', views.searchTemplateView, name="searchTemplate"),
    url(r'^addtemplate/(?P<course_id>\d+)/$', views.addTemplateView, name='addTmplate'),

    #user auth urls --> login and logout
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/$', views.register_user, name='register_user'),
    url(r'^accounts/register_success/$', views.register_success, name='register_success'),
)
