from annoying.decorators import render_to
from models import Lesson, Student
import datetime

@render_to('home.html')
def home(request):
    current_week = datetime.datetime.now().isocalendar()[0:2]
    lessons = Lesson.objects.all()
    filtered_lessons = []
    for lesson in lessons:
        if lesson.date.isocalendar()[0:2] == current_week:
            students = Student.objects.filter(group=lesson.group)
            filtered_lessons.append([lesson, students])


    return {'lessons': filtered_lessons}