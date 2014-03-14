from django.conf.urls import patterns, url

from GradeTracker import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.login, name='login'),
    url(r'^index', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),

    url(r'^(?P<student_id>\d+)/(?P<course_id>\d+)/$', views.grades, name='grades'),
    
    #Course modification 
    url(r'^deleteCourse/(?P<course_id>\d+)/$', views.deleteCourse, name='delete-course'),
    url(r'^editcourse/(?P<course_id>\d+)/$', views.editCourse, name='edit-course'),

#    url(r'(^?P<student_id>\d+)/(?P<course_id>\d+)/(?P<graded_activity_id>\d+)$', views.activity, name='activity'),
    
    url(r'^(?P<student_id>\d+)/test/$', views.test, name='test'),

    #user auth urls --> login and logout
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/$', views.register_user, name='register_user'),
    url(r'^accounts/register_success/$', views.register_success, name='register_success'),
)
