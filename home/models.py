from django.db import models
from django.contrib.auth.models import User


class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)  # Long integer, Primary Key
    branch_name = models.CharField(max_length=255)  # Varchar
    branch_abr = models.CharField(max_length=10)  # Varchar
    branch_floor = models.IntegerField()  # Long integer

    def __str__(self):
        return self.branch_name

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)  # Long integer, Primary Key
    subject_name = models.CharField(max_length=255)  # Varchar
    subject_abr = models.CharField(max_length=10)  # Varchar
    subject_credits = models.IntegerField()  # Long integer


    def __str__(self):
        return self.subject_name
    
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    name = models.CharField(max_length=255)  # Varchar
    t_staff_floor = models.IntegerField()
    t_staff_room = models.IntegerField()
    t_staff_layout = models.ImageField(upload_to="staffroom_layouts/")

    def __str__(self):
        return self.name

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=255)  # Varchar
    room_type = models.CharField(max_length=50)  # Varchar (e.g., Lecture Hall, Lab, etc.)
    room_floor = models.IntegerField()

    def __str__(self):
        return f'{self.room_type}:{self.room_name} on {self.room_floor}'
    
class Student(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # One-to-One relationship with User model
    # sap_id      = models.AutoField(primary_key=True)  # Long integer, Primary Key
    sap_id      = models.PositiveBigIntegerField(max_length=11, primary_key=True)  # Varchar, Primary Key
    roll_no     = models.CharField(max_length=4)
    name        = models.CharField(max_length=255)  # Varchar
    branch_id   = models.ForeignKey(Branch ,on_delete=models.CASCADE)  
    class_id    = models.CharField(max_length=2)
    section     = models.IntegerField()
    sem         = models.IntegerField()
    AY          = models.DateField()  # Academic Year

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

class Teaches(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Foreign Key to Teacher
    sub_id = models.ForeignKey(Subject,on_delete=models.CASCADE)  # Subject ID (e.g., SC01)
    sem = models.IntegerField()  # Semester
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE,)  # Foreign Key to Room
    class_id = models.CharField(max_length=2, )  # Class ID (e.g., C2)
    section = models.IntegerField(default=0)  # Section
    start_time = models.TimeField()  # Start Time
    end_time = models.TimeField()  # End Time
    day = models.CharField(max_length=20)  # Day (e.g., Monday, Tuesday)

    def __str__(self):
        return f"{self.teacher_id.name} teaches {self.sub_id} in {self.room_id.room_name} on {self.day}"
    
class BranchSub(models.Model):
    bs_id = models.AutoField(primary_key=True)  # Primary Key
    sub_id = models.ForeignKey(Subject, on_delete=models.CASCADE)  # Foreign Key to Subject
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)  # Foreign Key to Branch
    sem = models.IntegerField()  # Semester
    scheme = models.CharField(max_length=50)  # Scheme (e.g., CBCS, 2018)

    def __str__(self):
        return f"{self.branch_id.branch_name} - {self.sub_id.subject_name} (Sem {self.sem})"
    
