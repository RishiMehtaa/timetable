from django.shortcuts import render
from .models import *

# Create your views here.
def get_home(request):
    return render(request, 'home.html')

# TIMETABLE
# fetch a class's titmetable
# @api_view(['GET'])
# def get_class_timetable(request):
    # if request.method == 'GET':
    #     sem = request.GET.get('sem')
    #     class_id = request.GET.get('class_id')
    #     section = request.GET.get('section')
    #     if section == 'dono chahiye':
    #         timetable = Teaches.objects.filter(sem=sem,class_id=class_id)    
    #     else:
    #         timetable = Teaches.objects.filter(sem=sem,class_id=class_id,section=section)  

    #     timetable_list = []
    #     for t in timetable:
    #         timetable_list.append({
    #             'subject': t.sub_id.subject_abr,
    #             'teacher': t.teacher_id.name,
    #             'room': t.room_id.room_name,
    #             'day': t.day,
    #             'start_time': t.start_time,
    #             'end_time': t.end_time,
    #             'class_id': t.class_id,
    #             'section': t.section,
    #             'sem': t.sem,
    #         })  
        
    #     return render(request, 'timetable.html', {
    #     'timetable': timetable_list,
    #     'sem': sem,
    #     'class_id': class_id,
    #     'section': section})     #how to return, json or direct?
from collections import defaultdict
from datetime import time

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

        # Step 2: Create an empty table structure
        table_data = defaultdict(lambda: {day: "" for day in days})

        # Step 3: Populate table_data
        for entry in timetable:
            slot = (entry.start_time.strftime("%H:%M"), entry.end_time.strftime("%H:%M"))
            info = f"{entry.sub_id.subject_abr}<br>{entry.teacher_id.name}<br>{entry.room_id.room_name}"
            table_data[slot][entry.day] = info

        # Step 4: Sort time slots
        sorted_slots = sorted(table_data.items(), key=lambda x: x[0])
        
        return render(request, 'timetable.html', {
            'days': days,
            'time_slots': sorted_slots,
        })


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