from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Teaches)
admin.site.register(BranchSub)