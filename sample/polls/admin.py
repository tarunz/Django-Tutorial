from django.contrib import admin

from .models import Question, Choice
list_filter = ['pdate']
admin.site.register(Question)
admin.site.register(Choice)
# Register your models here.
