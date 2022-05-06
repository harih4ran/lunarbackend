from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework import viewsets
from .models import Hero
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
import json

class UserRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        heros = Hero.objects.all()
        serializer = HeroSerializer(heros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



#hero test
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
  

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignments.objects.all()
    serializer_class= AssignmentsSerializer
    


class DocumentViewSet(viewsets.ModelViewSet):  
    queryset  = Documents.objects.all()
    serializer_class= DocumentsSerializer

'''
class DocumentListViewSet(viewsets.ModelViewSet):  
    queryset  = DocumentList.objects.all()
    serializer_class= DocumentListSerializer




@api_view(['GET','POST'])
def getAssignments(request):
    assignments = Assignments.objects.all()
    serializer = AssignmentsSerializer(assignments, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getPosts(request):
    posts = Posts.objects.all()
    serializer = PostsSerializer(posts, many =True)
    return Response(serializer.data)
'''
# Create your views here.


@api_view(['POST'])
def registerUser(request):
    data = request.data
    user = User.objects.create(
        #first_name = data['name'],
        username=data['username'],
        #email=data['email'],
        #phoneNumber=data['phoneNumber'],
        #idnumber=data['idnumber'],
        #college=data['college'],
        #course=data['course'],
        #year_of_enrollment=data['year_of_enrollment'],
        #profile_photo=data['profile_photo'],
        #gender=data['gender'],
        #password=make_password(data['password'])
    )

    serializer = UserSerializerWithToken(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many =False)
    return Response(serializer.data)



@api_view(['GET'])
def getCourses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many =True)
    return Response(serializer.data)


class SessionViewSet(viewsets.ModelViewSet):
    queryset =  Session.objects.all()
    serializer_class= SessionSerializer
    
    
@api_view(['GET'])
def getStudent(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many =True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def getStudents(request):
    students = Students.objects.all()
    serializer = StudentsSerializer(students, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getTeacher(request):
    teacher = Teacher.objects.all()
    serializer = TeacherSerializer(teacher, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getSubject(request):
    subject = Subject.objects.all()
    serializer = SubjectSerializer(subject, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getResults(request):
    results = Results.objects.all()
    serializer = ResultsSerializer(results, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getAttendance(request):
    attendance = Attendance.objects.all()
    serializer = AttendanceSerializer(attendance, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def getAttendanceReport(request):
    attendanceReport = AttendanceReport.objects.all()
    serializer = AttendanceSerializer(attendanceReport, many =True)
    return Response(serializer.data)

@api_view(['GET'])
def getAppointment(request):
    appointment = Appointment.objects.all()
    serializer = AppointmentSerializer(appointment, many =True)
    return Response(serializer.data)


@api_view(['GET'])
def sessiondetails(request,course):
    heros = Hero.objects.filter(course=course)
    serializer = HeroSerializers(heros, many =True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response([])


@api_view(['GET'])
def assignmentdetails(request,course):
    assignments = Assignments.objects.filter(course=course)
    serializer = AssignmentSerializer(assignments, many =True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response([])

@api_view(['GET'])
def documentdetails(request,course):
    documents = Documents.objects.filter(course_name=course)
    serializer = DocumentSerializer(documents, many =True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response([])

@api_view(['GET'])
def alldocumentdetails(request,course,name):
    documents = Documents.objects.filter(course_name=course,name = name)
    serializer = DocumentSerializer(documents, many =True)
    if serializer.data:
        return Response(serializer.data)
    else:
        return Response([])

@api_view(['GET'])
def filterassignment(request,status):
    if status == "yes":
        assignments = Assignments.objects.filter(completed = True)
        serializer = AssignmentSerializer(assignments, many =True)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response([])
    elif status == "no":
        assignments = Assignments.objects.filter(completed = False)
        serializer = AssignmentSerializer(assignments, many =True)
        if serializer.data:
            return Response(serializer.data)
        else:
            return Response([])
    else:
            return Response([])

@api_view(['POST'])
def PostView(request):
    try:
        data=json.loads(request.POST['data'])
        photo = request.FILES.get('photo')
        Posts.objects.create(
            name = data['name'],
            description = data['description'],
            photo = photo
        )

        return Response(
            {
                "success": True,
                "details": "post created",
            },
        )
    except Exception as e:
        return Response({"status": False, "message": "Failed", "error": str(e)})


@api_view(['POST'])
def PostViewUpdate(request,postname):
    try:
        data=json.loads(request.POST['data'])
        photo = request.FILES.get('photo')
        Posts.objects.filter(name = postname).update(name = data['name'],description = data['description'],photo = photo)

        return Response(
            {
                "success": True,
                "details": "post updated",
            },
        )
    except Exception as e:
        return Response({"status": False, "message": "Failed", "error": str(e)})

@api_view(['POST'])
def PostViewDelete(request,postname):
    try:
        Posts.objects.filter(name = postname).delete()

        return Response(
            {
                "success": True,
                "details": "post deleted",
            },
        )
    except Exception as e:
        return Response({"status": False, "message": "Failed", "error": str(e)})


@api_view(['POST'])
def AssignmentView(request):
    try:
        data=json.loads(request.POST['data'])
        photo = request.FILES.get('photo')
        Assignments.objects.create(
            course = data['course_name'],
            due = data['due_date'],
            attachment = photo
        )

        return Response(
            {
                "success": True,
                "details": "assignment created",
            },
        )
    except Exception as e:
        return Response({"status": False, "message": "Failed", "error": str(e)})


@api_view(['POST'])
def SessionView(request):
    try:
        data = request.data
        Session.objects.create(
            course_name = data['course_name'],
            tutor = data['tutor'],
            course_code =  data['course_code'],
            venue =  data['venue'],
            phone_no =  data['phone_no'],
            assistance_tutor =  data['assistance_tutor'],
            total_students =  data['total_students'],
        )

        return Response(
            {
                "success": True,
                "details": "session created",
            },
        )
    except Exception as e:
        return Response({"status": False, "message": "Failed", "error": str(e)})

@api_view(['POST'])
def SessionViewDelete(request,id):
    try:
        Session.objects.filter(id = id).delete()

        return Response(
            {
                "success": True,
                "details": "session deleted",
            },
        )
    except Exception as e:
        return Response({"status": False, "message": "Failed", "error": str(e)})
