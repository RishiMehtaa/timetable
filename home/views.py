from django.shortcuts import render
from .models import *

# Create your views here.

# TIMETABLE
# fetch a class's titmetable
# @api_view(['GET'])
def get_class_timetable(request,sem,class_id,section):
    if section == 'dono chahiye':
        timetable = Teaches.objects.filter(sem=sem,class_id=class_id)    
    else:
        timetable = Teaches.objects.filter(sem=sem,class_id=class_id,section=section)  

    timetable_list = []
    for t in timetable:
        subject = Subject.objects.get(id=t.sub_id)
        teacher = Teacher.objects.get(id=t.teacher_id)
        room = Room.objects.get(id=t.room_id)
        timetable_list.append({
            'subject': subject.subject_abr,
            'teacher': teacher.name,
            'room': room.room_name,  # what to display????????
            'day': t.day,
            'start_time': t.start_time,
            'end_time': t.end_time,
            'class_id': t.class_id,
            'section': t.section,
            'sem': t.sem,
        })  
    return render(request, 'timetable.html', {'timetable': timetable_list})     #how to return, json or direct?
# fetch a teacher's timetable
# fetch a room's timetable


# TEACHER PROFILE
# fetch which all subjects a teacher teaches along with sem
## fetch which all classes a teacher teaches 
# fetch which branches a teacher teaches in
# fetch floor, staff room and layout of the teacher's staff room

# CLASS PROFILE
# fetch which all teachers teach a class with sub
## fetch which students are there in a class

# SUBJECTS
# fetch which all teachers teach a subject
# fetch credits
# fetch the days on which the subject is taught and how many times

# BRANCH
# fetch which all subjects are there in a branch
# fetch which all teachers are there in a branch
# fetch which floor a branch is

# STUDENTS
# fetch everything


# fetch classes which have remedial on particular day