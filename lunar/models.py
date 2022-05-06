from django.db import models
from django.contrib.auth.models import User

#Student model
class Students(models.Model):
    first_name = models.CharField(max_length=200,null=True,blank=True)
    username=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    phoneNumber=models.CharField(max_length=200,null=True,blank=True)
    student_id=models.CharField(max_length=200,null=True,blank=True)
    college=models.CharField(max_length=200,null=True,blank=True)
    course= models.CharField(max_length=200,null=True,blank=True)
    year_of_enrollment=models.CharField(max_length=200,null=True,blank=True)
    profile_photo=models.CharField(max_length=200,null=True,blank=True)
    gender=models.CharField(max_length=200,null=True,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
            return self.email

#hero model
class Hero(models.Model):
    name = models.CharField(max_length=60,null=True)
    alias = models.CharField(max_length=60,null=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    username=models.CharField(max_length=200,null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    phoneNumber=models.CharField(max_length=200,null=True,blank=True)
    student_id=models.CharField(max_length=200,null=True,blank=True)
    college=models.CharField(max_length=200,null=True,blank=True)
    course= models.CharField(max_length=200,null=True,blank=True)
    year_of_enrollment=models.CharField(max_length=200,null=True,blank=True)
    profile_photo=models.CharField(max_length=200,null=True,blank=True)
    gender=models.CharField(max_length=200,null=True,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)
      
    def __str__(self):
        return self.name

#Course model
class Course(models.Model):
    course_code = models.IntegerField()
    course_name = models.CharField(max_length=200, null=True, blank=True)
    course_total = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.course_name

#Class model
class Session(models.Model):
    course_name = models.CharField(max_length=200,blank=True, null= True,default="DEFAULT VALUE")
    tutor = models.CharField(max_length=200,null=False,blank=True)
    course_code = models.IntegerField()
    venue = models.CharField(max_length=200,null=False,blank=True)
    time = models.TimeField(auto_now = True)
    phone_no = models.IntegerField()
    assistance_tutor = models.CharField(max_length=200,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    total_students =  models.IntegerField(default = 0)

    def __str__(self):
        return self.course_name

#Student model
class Student(models.Model):
    student_id =models.IntegerField()
    student_group = models.CharField(max_length=200,null=True,blank=True)
    student_name = models.CharField(max_length=200,null=True,blank=True)
    student_class_code = models.IntegerField(null=True, blank=True,default=0)
    student_total =  models.IntegerField(null=True,blank=True,default=0)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.student_group

#Teacher model
class Teacher(models.Model):
    Teacher_id =models.IntegerField()
    Teacher_name = models.CharField(max_length=200,null=True,blank=True)
    Teacher_subject = models.CharField(max_length=200, null=True, blank = True)
    Teacher_total =  models.IntegerField(null=True,blank=True,default=0)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.Teacher_name

 #Subject model
class Subject(models.Model):
    Subject_id =models.IntegerField()
    Subject_name = models.CharField(max_length=200,null=True,blank=True)
    Subject_Teacher = models.CharField(max_length=200, null=True, blank = True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.Subject_name

#Results model
class Results(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)
    subject_assignment_marks = models.FloatField(default=0)
    id = models.AutoField(primary_key=True,editable=False)
    objects = models.Manager()

    def __str__(self):
        return self.subject_assignment_marks


 #Attendance model  
class Attendance(models.Model):
    Subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    Attendance_date = models.DateField()
    Student_id =models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.Attendance_date

#Attendance Report model
class AttendanceReport(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    Attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.Attendance_id

#Appointment model
class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    appointment_date = models.CharField(max_length=255)
    appointment_message = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.appointment_message



class Posts(models.Model):
    description = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    avater = models.ImageField(null=True, blank=True)
    photo = models.FileField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Documents(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    name_doc= models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    attachment = models.FileField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    course_name = models.CharField(max_length=200,blank=True, null= True)

    def __str__(self):
        return str(self.name)
'''
  #  @property
    def doxlist(self):
        return self.dox_List.all()

class DocumentList(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    attachment = models.FileField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)
    documents = models.ManyToManyField(Documents, related_name= "documents")

    def __str__(self):
        return str(self.name)

'''



class Assignments(models.Model):
    course = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    due = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.course)



