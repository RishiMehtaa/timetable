from collections import defaultdict
from datetime import datetime
from datetime import time
from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, StudentProfileForm

def student_register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = StudentProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def student_logout(request):
    logout(request)
    return redirect('home')

def parse_time(s):
    return datetime.strptime(s, "%H:%M")

def time_diff_in_slots(start, end):
    return int((end - start).seconds / 60) // 30

all_slots = [
    ("08:00", "08:30"), ("08:30", "09:00"),
    ("09:00", "09:30"), ("09:30", "10:00"),
    ("10:00", "10:30"), ("10:30", "11:00"),
    ("11:00", "11:30"), ("11:30", "12:00"),
    ("12:00", "12:30"), ("12:30", "13:00"),
    ("13:00", "13:30"), ("13:30", "14:00"),
    ("14:00", "14:30"), ("14:30", "15:00"),
    ("15:00", "15:30"), ("15:30", "16:00"),
    ("16:00", "16:30"), ("16:30", "17:00"),
    ("17:00", "17:30"), ("17:30", "18:00"),
]
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
        
        # Fetching data
        if section == 'dono chahiye':
            timetable = Teaches.objects.filter(sem=sem, class_id=class_id)
        else:
            timetable = Teaches.objects.filter(sem=sem, class_id=class_id, section=section ) |  Teaches.objects.filter(sem=sem, class_id=class_id, section=0)
        
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        table_data = defaultdict(lambda: {day: {"info": "", "span": 1, "show": True} for day in days})

        for entry in timetable:
            start = entry.start_time.strftime("%H:%M")
            end = entry.end_time.strftime("%H:%M")
            start_dt = parse_time(start)
            end_dt = parse_time(end)
            slot_count = time_diff_in_slots(start_dt, end_dt)
            
            info = f"{entry.sub_id.subject_abr}<br>{entry.teacher_id.name}<br>{entry.room_id.room_name}"

            # Find the index of the start time in all_slots
            for i, (slot_start, slot_end) in enumerate(all_slots):
                if slot_start == start:
                    # If "dono chahiye", append info for both sections
                    if section == 'dono chahiye':
                        existing_info = table_data[(slot_start, slot_end)][entry.day]["info"]
                        if existing_info:
                            # Append the new info directly to the existing info
                            table_data[(slot_start, slot_end)][entry.day]["info"] += f"<br>{info}"
                            
                            
                        else:
                            # Initialize the cell with the current info
                            table_data[(slot_start, slot_end)][entry.day]["info"] = info
                        table_data[(slot_start, slot_end)][entry.day]["span"] = slot_count
                        table_data[(slot_start, slot_end)][entry.day]["show"] = True
                    else:
                    # Mark the first cell with info and rowspan
                        table_data[(slot_start, slot_end)][entry.day] = {
                            "info": info,
                            "span": slot_count,
                            "show": True
                        }
                    # table_data[(slot_start, slot_end)][entry.day] = {
                    #         # "info": info,
                    #         "span": slot_count,
                    #         "show": True
                    #     }

                    # Hide the rest of the cells in that span
                    for j in range(1, slot_count):
                        if i + j < len(all_slots):
                            hidden_slot = all_slots[i + j]
                            table_data[hidden_slot][entry.day] = {
                                "info": "",
                                "span": 1,
                                "show": False
                            }
                    break  # Done with this entry

        return render(request, 'timetable.html', {
            'days': days,
            'time_slots': table_data,
            'predefined_time_slots': all_slots,
        })

# def get_class_timetable(request):
#     if request.method == 'GET':
#         sem = request.GET.get('sem')
#         class_id = request.GET.get('class_id')
#         section = request.GET.get('section')
#         if section == 'dono chahiye':
#             timetable = Teaches.objects.filter(sem=sem,class_id=class_id)    
#         else:
#             timetable = Teaches.objects.filter(sem=sem,class_id=class_id,section=section)  
#         # Days for header row
#         days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

#         table_data = defaultdict(lambda: {day: "" for day in days})

#         for entry in timetable:
#             slot = (entry.start_time.strftime("%H:%M"), entry.end_time.strftime("%H:%M"))
#             info = f"{entry.sub_id.subject_abr}<br>{entry.teacher_id.name}<br>{entry.room_id.room_name}"
#             table_data[slot][entry.day] = info

#         sorted_slots = sorted(table_data.items(), key=lambda x: x[0])
#         # print(sorted_slots)
#         # print(table_data)

#         return render(request, 'timetable.html', {
#             'days': days,
#             'time_slots': table_data,
#             'predefined_time_slots': all_slots,
#         })

# fetch a teacher's timetable
def get_teacher_timetable(request):
    if request.method == 'GET':
        teacher_id = request.GET.get('teacher_id')
        timetable = Teaches.objects.filter(teacher_id=teacher_id)  
        # Days for header row
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        # table_data = defaultdict(lambda: {day: "" for day in days})
        table_data = defaultdict(lambda: {day: {"info": "", "span": 1, "show": True} for day in days})


        # for entry in timetable:
        #     slot = (entry.start_time.strftime("%H:%M"), entry.end_time.strftime("%H:%M"))
        #     info = f"{entry.sub_id.subject_abr}<br>{entry.sem}{entry.class_id}<br>{entry.room_id.room_name}"
        #     table_data[slot][entry.day] = info


        # return render(request, 'teacher.html', {
        #     'days': days,
        #     'time_slots': table_data,
        #     'predefined_time_slots': all_slots,
        # })
        for entry in timetable:
            start = entry.start_time.strftime("%H:%M")
            end = entry.end_time.strftime("%H:%M")
            start_dt = parse_time(start)
            end_dt = parse_time(end)
            slot_count = time_diff_in_slots(start_dt, end_dt)
            
            info = f"{entry.sub_id.subject_abr}<br>{entry.sem}{entry.class_id}<br>{entry.room_id.room_name}"

            # Find the index of the start time in all_slots
            for i, (slot_start, slot_end) in enumerate(all_slots):
                if slot_start == start:
                    # Mark the first cell with info and rowspan
                    table_data[(slot_start, slot_end)][entry.day] = {
                        "info": info,
                        "span": slot_count,
                        "show": True
                    }
                    # Hide the rest of the cells in that span
                    for j in range(1, slot_count):
                        if i + j < len(all_slots):
                            hidden_slot = all_slots[i + j]
                            table_data[hidden_slot][entry.day] = {
                                "info": "",
                                "span": 1,
                                "show": False
                            }
                    break  # Done with this entry

        return render(request, 'teacher.html', {
            'days': days,
            'time_slots': table_data,
            'predefined_time_slots': all_slots,
        })

# fetch a room's timetable
def get_room_lab_timetable(request):
    if request.method == 'GET':
        room_id = request.GET.get('room_id')
        timetable = Teaches.objects.filter(room_id=room_id)  
        # Days for header row
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        table_data = defaultdict(lambda: {day: "" for day in days})

        for entry in timetable:
            start = entry.start_time.strftime("%H:%M")
            end = entry.end_time.strftime("%H:%M")
            start_dt = parse_time(start)
            end_dt = parse_time(end)
            slot_count = time_diff_in_slots(start_dt, end_dt)
            
            info = f"{entry.sub_id.subject_abr}<br>{entry.teacher_id.name}<br>{entry.sem}{entry.class_id}"

            # Find the index of the start time in all_slots
            for i, (slot_start, slot_end) in enumerate(all_slots):
                if slot_start == start:
                    # Mark the first cell with info and rowspan
                    table_data[(slot_start, slot_end)][entry.day] = {
                        "info": info,
                        "span": slot_count,
                        "show": True
                    }
                    # Hide the rest of the cells in that span
                    for j in range(1, slot_count):
                        if i + j < len(all_slots):
                            hidden_slot = all_slots[i + j]
                            table_data[hidden_slot][entry.day] = {
                                "info": "",
                                "span": 1,
                                "show": False
                            }
                    break  # Done with this entry

        return render(request, 'room_lab.html', {
            'days': days,
            'time_slots': table_data,
            'predefined_time_slots': all_slots,
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