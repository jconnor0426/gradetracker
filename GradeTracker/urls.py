from django.conf.urls import patterns, url

from GradeTracker import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<student_id>\d+)/$', views.detail, name='detail'),

    url(r'^(?P<student_id>\d+)/(?P<course_id>\d+)/$', views.grades, name='grades'),

    url(r'^deleteCourse/(?P<course_id>\d+)/$', views.deleteCourse, name='delete-course'),
    
    url(r'^main/$', views.main, name='main'),

    url(r'^(?P<student_id>\d+)/test/$', views.test, name='test'),
)
