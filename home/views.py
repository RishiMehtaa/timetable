from collections import defaultdict
from datetime import time
from django.shortcuts import render
from .models import *

# Create your views here.
def get_home(request):
    return render(request, 'home.html')

# TIMETABLE
# fetch a class's titmetable
def get_class_timetable(request):
    if request.method == 'GET':
        sem = request.GET.get('sem')
        class_id = request.GET.get('class_id')
        section = request.GET.get('section')
        if section == 'dono chahiye':
            timetable = Teaches.objects.filter(sem=sem,class_id=class_id)    
        else:
            timetable = Teaches.objects.filter(sem=sem,class_id=class_id,section=section)  
        # Days for header row
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        all_slots = [
            ("08:00", "09:00"),
            ("09:00", "10:00"),
            ("10:00", "11:00"),
            ("11:00", "12:00"),
            ("12:00", "13:00"),
            ("14:00", "15:00"),
            ("15:00", "16:00"),
        ]

        table_data = defaultdict(lambda: {day: "" for day in days})

        for entry in timetable:
            slot = (entry.start_time.strftime("%H:%M"), entry.end_time.strftime("%H:%M"))
            info = f"{entry.sub_id.subject_abr}<br>{entry.teacher_id.name}<br>{entry.room_id.room_name}"
            table_data[slot][entry.day] = info

        sorted_slots = sorted(table_data.items(), key=lambda x: x[0])

        return render(request, 'timetable.html', {
            'days': days,
            'time_slots': sorted_slots,
        })

# fetch a teacher's timetable
def get_teacher_timetable(request):
    if request.method == 'GET':
        teacher_id = request.GET.get('teacher_id')
        timetable = Teaches.objects.filter(teacher_id=teacher_id)  
        # Days for header row
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        all_slots = [
            ("08:00", "09:00"),
            ("09:00", "10:00"),
            ("10:00", "11:00"),
            ("11:00", "12:00"),
            ("12:00", "13:00"),
            ("14:00", "15:00"),
            ("15:00", "16:00"),
        ]

        table_data = defaultdict(lambda: {day: "" for day in days})

        for entry in timetable:
            slot = (entry.start_time.strftime("%H:%M"), entry.end_time.strftime("%H:%M"))
            info = f"{entry.sub_id.subject_abr}<br>{entry.sem}{entry.class_id}<br>{entry.room_id.room_name}"
            table_data[slot][entry.day] = info

        sorted_slots = sorted(table_data.items(), key=lambda x: x[0])

        return render(request, 'teacher.html', {
            'days': days,
            'time_slots': sorted_slots,
        })
# fetch a room's timetable
def get_room_lab_timetable(request):
    if request.method == 'GET':
        room_id = request.GET.get('room_id')
        timetable = Teaches.objects.filter(room_id=room_id)  
        # Days for header row
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        all_slots = [
            ("08:00", "09:00"),
            ("09:00", "10:00"),
            ("10:00", "11:00"),
            ("11:00", "12:00"),
            ("12:00", "13:00"),
            ("14:00", "15:00"),
            ("15:00", "16:00"),
        ]

        table_data = defaultdict(lambda: {day: "" for day in days})

        for entry in timetable:
            slot = (entry.start_time.strftime("%H:%M"), entry.end_time.strftime("%H:%M"))
            info = f"{entry.sub_id.subject_abr}<br>{entry.teacher_id.name}<br>{entry.sem}{entry.class_id}"
            table_data[slot][entry.day] = info

        sorted_slots = sorted(table_data.items(), key=lambda x: x[0])

        return render(request, 'room_lab.html', {
            'days': days,
            'time_slots': sorted_slots,
        })


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