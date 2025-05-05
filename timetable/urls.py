"""
URL configuration for timetable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.urls import path
from home.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', student_register, name='register'),
    path('login/', student_login, name='login'),
    path('logout/', student_logout, name='logout'),
    path('profile/', student_profile, name='profile'),
    path('', get_home, name='home'),
    path('timetable/',get_class_timetable,name='timetable'),
    path('mytimetable/', get_class_timetable, name='mytimetable'),
    # path('timetable/<int:sem>/<str:class_id>/<str:section>/', get_class_timetable, name='class_timetable'),
    path('teacher/', get_teacher_timetable, name='teacher'),
    path('teacher_profile/<int:pk>/', teacher_profile, name='teacher_profile'),
    path('room_lab/', get_room_lab_timetable, name='room_lab'),
    path('room-status/', room_status, name='room_status'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     path('timetable/', get_class_timetable, name='timetable'),
# ]
