from django.contrib import admin
from GradeTracker.models import Student,Course,Graded_Activities,SubGraded_Activities, Templates

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Graded_Activities)
admin.site.register(SubGraded_Activities)
admin.site.register(Templates)
