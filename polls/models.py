from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question.question_text}-{self.choice_text}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    dob = models.DateField()
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    student_image = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Interview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)  # HCL software Trinee
    mode = models.CharField(max_length=20)  # online or offline
    sub_mode = models.CharField(max_length=20)  # mock. group, exeam
    marks = models.FloatField()
    max_marks = models.IntegerField(default=100)
    result = models.CharField(max_length=10)  # pass, not-clear

    def __str__(self):
        return f"{self.student.first_name}-{self.name}-{self.result}"




from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,max_length=10,blank=True,null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=120)
    email = models.EmailField()
    address = models.TextField()
    pincode = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)



from django.contrib.auth.models import User



class Vehicle(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reg_num = models.CharField(max_length=20)
    reg_date = models.DateField()
    engine_num = models.CharField(max_length=50)
    chassis_num = models.CharField(max_length=50)
    rc = models.FileField(upload_to="vehicle/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reg_num}-{self.reg_date}"


class Email(models.Model):
    from_email = models.EmailField(help_text="from email")
    to_email = models.EmailField(help_text="To email")
    subject = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.subject

class Firstclass(models.Model):
    class_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40,null=True,blank=True)
    email = models.CharField(max_length=255)


