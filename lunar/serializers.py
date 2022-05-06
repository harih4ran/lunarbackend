from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import UniqueTogetherValidator
from django.utils.dateparse import parse_datetime
from django.contrib.humanize.templatetags import humanize
from .models import  Hero,Posts,Assignments,Documents,Course,Session,Student,Students,Teacher,Subject,Results,Attendance,AttendanceReport,Appointment


#User serializer

#class UserSerializer(serializers.ModelSerializer):
   # name = serializers.SerializerMethodField(read_only=True)
 #   class Meta:
  #      model = User
   #     fields = ['id','username','email']
   


"""class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['id', 'password']
            )
        ]

"""


"""class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
  
    class Meta:
        model = User
        fields = '__all__'
        #['id','_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

"""

#hero
class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class  PostsSerializer(serializers.HyperlinkedModelSerializer):
    datehumanize = serializers.SerializerMethodField('dateHumanize')

    def dateHumanize(self,obj):
        formatted_time = humanize.naturaltime(obj.createdAt)
        return str(formatted_time)
    
    
    class Meta:
        model = Posts
        fields = '__all__'



#Assignments serializer
class  AssignmentsSerializer(serializers.HyperlinkedModelSerializer):
    getcreatedat = serializers.SerializerMethodField('getCreatedAt')
    getdue = serializers.SerializerMethodField('getDue')

    def getCreatedAt(self,obj):
        formatted_time = parse_datetime(str(obj.createdAt)).strftime('%d-%m-%Y')
        return str(formatted_time)

    def getDue(self,obj):
        try:
            formatted_time = parse_datetime(str(obj.due)).strftime('%d-%m-%Y')
            return str(formatted_time)
        except:
            return "None"
    
    class Meta:
        model =  Assignments
        fields = '__all__'



'''
class DocumentListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = DocumentList
        fields = '__all__'
'''
#Documents serializer
class  DocumentsSerializer(serializers.HyperlinkedModelSerializer):
  #  documents = DocumentListSerializer(many = True)


    class Meta:
        model = Documents
        fields = '__all__'


    #def get_avater(self, obj):
     # return obj.avater.url

"""
    def create(self, validated_data):
        hero = Hero.objects.create_hero(**validated_data)
        return hero

    class Meta:
        model = Hero
        fields = '__all__' 
        validators = [
            UniqueTogetherValidator(
                queryset=Hero.objects.all(),
                fields=['id', 'password']
            )
        ]


"""





#course serializer

class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = '__all__'


#Session serializer
class SessionSerializer(serializers.ModelSerializer):
    getdate = serializers.SerializerMethodField('getDate')

    def getDate(self,obj):
        formatted_time = parse_datetime(str(obj.date)).strftime('%d-%m-%Y')
        return str(formatted_time)
    
    class Meta:
        model = Session
        fields = '__all__'


#student serializer
class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
#student serializer

class StudentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        fields = '__all__'


        
#Teacher serializer
class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teacher
        fields = '__all__'

#Subject serializer
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = '__all__'

#Results serializer
class  ResultsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Results
        fields = '__all__'



#Attendance serializer
class AttendanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Attendance
        fields = '__all__'

#AttendanceReport serializer
class AttendanceReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   AttendanceReport
        fields = '__all__'


#Appointment serializer
class  AppointmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =   Appointment
        fields = '__all__'


'''
#Posts serializer
class  PostsSerializer(serializers.ModelSerializer):
    
    avater = serializers.ImageField(use_url = True)
    #avater = serializers.SerializerMethodField('get_avater')

    class Meta:
        model = Posts
        fields = '__all__'

    #def get_avater(self, obj):
     # return obj.avater.url

'''

class HeroSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Hero
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    getcreatedat = serializers.SerializerMethodField('getCreatedAt')
    getdue = serializers.SerializerMethodField('getDue')

    def getCreatedAt(self,obj):
        formatted_time = parse_datetime(str(obj.createdAt)).strftime('%d-%m-%Y')
        return str(formatted_time)

    def getDue(self,obj):
        formatted_time = parse_datetime(str(obj.due)).strftime('%d-%m-%Y')
        return str(formatted_time)
    
    class Meta:
        model = Assignments
        fields = '__all__'

  

    
class DocumentSerializer(serializers.ModelSerializer):
    getcreatedat = serializers.SerializerMethodField('getCreatedAt')

    def getCreatedAt(self,obj):
        formatted_time = parse_datetime(str(obj.createdAt)).strftime('%d-%m-%Y')
        return str(formatted_time)

    class Meta:
        model = Documents
        fields = '__all__'