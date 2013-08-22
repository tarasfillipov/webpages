from django.contrib import admin
from models import Lesson,Student,Group

class LessonAdmin(admin.ModelAdmin):
    list_display = ['title','date']

admin.site.register(Lesson, LessonAdmin)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'group']

admin.site.register(Student, StudentAdmin)

class GroupAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Group, GroupAdmin)
