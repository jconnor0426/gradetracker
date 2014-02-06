from django.contrib import admin
from polls.models import Question

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields':['question_text']}),
    ('Date information', {'fields':['pub_date']}),
  ]

admin.site.register(Question, PollAdmin)
