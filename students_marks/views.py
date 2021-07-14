

# Create your views here.
from django.db.models.aggregates import Avg
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from .models import students
from .serializers import StudentSerializer
from django.db.models import Sum
# Create your views here.

class StudentCreateMark(APIView):
    
    def post(self,request):
        try:
            data= request.data
            student_name = (data.get("name"))
            #subject = (data.get("subject"))
            #marks = data.get("marks")
            
            #dictionary = dict()
            student_details = data.get("marks")
            for i in data["marks"].keys(): 
                student_new, created = students.objects.update_or_create(name=student_name,subject =i,
                                                                     defaults={'marks':student_details[i]
                                                                     })

            return Response(
                    status=status.HTTP_200_OK,
                    data={'data':"Created Successfully",
                    'status':status.HTTP_200_OK}
                )

        except Exception as e:
            print(str(e))
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error':str(e)}
            )

class GetStudentsMark(APIView):
    
    def get(self,request,pk):
        try:
            #allmark = students.objects.exclude("marks")
            
            student_obj = students.objects.filter(name = pk)            #print(student_obj)
            
            all_marks = []
            for i in student_obj:
                all_marks.append(i.marks)
            data_obj = {pk:all_marks}
               
            return Response(
                    status=status.HTTP_200_OK,
                    data= data_obj
                )

        except Exception as e:
            print(str(e))
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error':str(e)}
            )

class GetStudentTotalMark(APIView):
    
    def get(self,request):
        try:
            #all_students = []
            all_students = dict()
            

            #length = students.objects.all().count()
            #student_all = students.objects.all()
            #student_count = students.objects.all().distinct("name").count()
            #num_of_students = length/student_count
            student_name = students.objects.all().distinct("name")
            for names in student_name:
                student1 = students.objects.filter(name = names.name).aggregate(total_marks = Sum("marks"))
                all_students[names.name] = student1
                #all_students.append(data_obj)
            
            return Response(
                    status=status.HTTP_200_OK,
                    data=all_students
                )
            
        except Exception as e:
            print(str(e))
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error':str(e)}
            )

class GetAverageMark(APIView):
    
    def get(self,request):
        try:
            student_name = students.objects.all().distinct("name")
            all_students =dict()
            for names in student_name:
                student1 = students.objects.filter(name = names.name).aggregate(Average_marks = Avg("marks"))
                all_students[names.name] = student1
            
            return Response(
                    status=status.HTTP_200_OK,
                    data= all_students
                )
            
            
        except Exception as e:
            print(str(e))
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={'error':str(e)}
            )