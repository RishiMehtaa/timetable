from django import forms
from django.contrib import admin
from django.forms.widgets import TimeInput
from .models import *

class TeachesAdminForm(forms.ModelForm):
    class Meta:
        model = Teaches
        fields = '__all__'
        widgets = {
            'start_time': TimeInput( attrs={'type': 'time', 'step': 1800}),
            'end_time': TimeInput(attrs={'type': 'time', 'step': 1800}),
        }

class TeachesAdmin(admin.ModelAdmin):
    form = TeachesAdminForm
    
# Register your models here.
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Room)
admin.site.register(Student)
admin.site.register(Teaches,TeachesAdmin)
admin.site.register(BranchSub)