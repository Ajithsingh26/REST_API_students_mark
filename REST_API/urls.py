from django.conf.urls import include, url 
from django.contrib import admin

import students_marks
from django.urls import path 
from students_marks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('/',include("students_marks.urls"))
    path('createmark/', views.StudentCreateMark.as_view(), name='studentCreateMark'),
    path('getallmark/<str:pk>', views.GetStudentsMark.as_view(), name='GetStudentsMark'),
    path('gettotalmark/', views.GetStudentTotalMark.as_view(), name='GetStudentTotalMark'),
    path('getaveragemark/', views.GetAverageMark.as_view(), name='GetStudentAverageMark'),
]