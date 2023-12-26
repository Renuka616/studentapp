from django.http import HttpResponseRedirect
# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse


def data_render(request):
    data = [
        {"gender": "male", "fname": "suresh", "lname": "kumar", "age": 23, "tech": ["c,python"]},
        {"gender": "female", "fname": "renuka", "lname": "reddy", "age": 23, "tech": ["Django,python"]},
        {"gender": "male", "fname": "mahesh", "lname": "kumar", "age": 23, "tech": ["selenium,python"]},
        {"gender": "female", "fname": "sundhya", "lname": "kumari", "age": 23, "tech": ["c,networking"]},
    ]
    return render(request, template_name="polls/render.html", context={"mydata":data})

from .models import Question

def questions_list(request):
    questions = Question.objects.all()
    return render(request, template_name="qc/question.html",context={"questions": questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, template_name="qc/detail_question.html",
                  context={"question": question})

# there is a way to interact with django project.
# we saw all entries which were there in db.
from .models import Student
def student_list(request):
    students = Student.objects.all()
    return render(request, template_name="student/student_list.html", context={"students":students})

def student_detail(request,pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, template_name="student/student_detail.html", context={"student":student})



def create_student(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        student = Student.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            dob=request.POST["my-dob"],
            mobile=request.POST["mobile"],
            gender=request.POST["gender"],
            student_image=request.FILES["profile_pic"]
        )
        return HttpResponseRedirect(reverse("polls:student-list", args=[]))
    else:
        return render(request, template_name="student/create_student.html", context={})


def user_list(request):
    user = User.objects.all()
    return render(request, template_name="user/user_list.html", context={"user":user})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, template_name="user/user_detail.html", context={"user":user})

def create_user(request):
    if request.method == "POST":
        user = User.objects.create(
            username=request.POST["username"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            password=request.POST["password"]
        )
        return HttpResponseRedirect(reverse("polls:list-user", args=[]))
    else:
        return render(request, template_name="user/create_user.html", context={})


def folder_a(request):
    return render(request, template_name="folderA/a/fa1.html",context={})


def folder_aa(request):
    return render(request, template_name="folderA/a/fa2.html",context={})

def folderb(request):
    return render(request, template_name="folderB/a1.html",context={})

def folderb1(request):
    return render(request, template_name="folderB/b1.html",context={})

from polls.models import Customer
def customer_list(request):
    customer = Customer.objects.all()
    return render(request, template_name="customer/customer_list.html", context={"customer":customer})

from django.contrib.auth.decorators import login_required
@login_required(login_url="/polls/login/")
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, template_name="customer/customer_detail.html", context={"customer":customer})

def create_customer(request):
    if request.method == "POST":
        customer = Customer.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            short_name=request.POST["short_name"],
            email=request.POST["email"],
            address=request.POST["address"],
            mobile=request.POST["mobile"]

        )
        return HttpResponseRedirect(reverse("polls:customer-list", args=[]))
    else:
        return render(request, template_name="customer/create_customer.html", context={})

from .form import CustomerForm
def df_customer_create_view(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return HttpResponseRedirect(reverse("polls:customer-detail", args=(customer.id, )))
    else:
        form = CustomerForm()
    return render(request, template_name="customer/df_create_customer.html", context={"form": form})
def df_customer_update_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":

        form = CustomerForm(request.POST, instance=customer)
        # form validate
        if form.is_valid():
            # obj = form.save(commit=False)
            # do some operations
            # obj.save()
            customer = form.save()
            return HttpResponseRedirect(reverse("polls:customer-detail", args=(customer.id, )))
            # return redirect("polls:customer-detail")
    else:
        form = CustomerForm(instance=customer)

    return render(request, template_name="customer/df_update.html", context={"form": form})



from .form import VehicleForm
def create_vehicle(request):
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save()
            return HttpResponseRedirect(reverse("polls:customer-detail", args=(vehicle.customer.pk, )))
    else:
        form = VehicleForm()

    return render(request, template_name="vehicle/create.html", context={"form": form})




from .form import SignupForm
from django.contrib.auth.models import User
def signup(request):
    if request.method == "POST":
        #import pdb;pdb.set_trace()
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                password=form.cleaned_data["password"]
            )
            return HttpResponseRedirect(reverse("polls:login", args=tuple()))
    else:
        form = SignupForm()
    return render(request, template_name="auth/signup.html", context={"form": form})

from .form import Login
from django.contrib.auth import authenticate,login
def user_login(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("polls:customer-list", args=tuple()))
            else:
                return render(request, template_name="auth/login.html", context={"form": form, "err": "Invalid User"})
        else:
            return render(request, template_name="auth/login.html", context={"form": form})
    else:
        form = Login()
        return render(request, template_name="auth/login.html", context={"form": form})



from .models import Email
def email_list(request):
    email = Email.objects.all()
    return render(request, template_name="email/email_list.html", context={"email":email})

def email_detail(request, pk):
    email = get_object_or_404(Email, pk=pk)
    return render(request, template_name="email/email_detail.html", context={"email":email})

def email_create(request):
    if request.method == "POST":
        email = Email.objects.create(
            from_email = request.POST["from_email"],
            to_email = request.POST["to_email"],
            subject = request.POST["subject"],
            body = request.POST["body"]
        )
        return HttpResponseRedirect(reverse("polls:email-list", args=[]))
    else:
        return render(request, template_name="email/email_create.html", context={})

from .models import Firstclass
def firstclass_list(request):
    firstclass = Firstclass.objects.all()
    return render(request, template_name="Class/class_list.html", context={"firstclass":firstclass})