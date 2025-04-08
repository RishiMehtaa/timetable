from django.db import models

class Student(models.Model):
    sap_id = models.IntegerField(primary_key=True)  # Long integer, Primary Key
    roll_no = models.CharField(max_length=4)
    name = models.CharField(max_length=255)  # Varchar
    branch_id = models.IntegerField()  # Foreign Key placeholder (can be linked to another model later)
    class_id = models.CharField(max_length=2)
    section = models.IntegerField()
    sem = models.IntegerField()
    AY = models.DateField()  # Academic Year

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
