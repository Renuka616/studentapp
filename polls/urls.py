from django.urls import path
from . import views
from . import generic_views
app_name = "polls"
urlpatterns = [
    path("mydata/",views.data_render,name="my-data"),
    path("question/list/",views.questions_list,name="question-list"),
    path("question/detail/<int:pk>/",views.question_detail,name="question-detail"),
    # student
    path("student/list/",views.student_list,name="student-list"),
    path("student/detail/<int:pk>/",views.student_detail,name="detail-student"),
    path("student/create/",views.create_student,name="create-student"),
    # user
    path("user/list/",views.user_list,name="list-user"),
    path("user/detail/<int:pk>/",views.user_detail,name="detail-user"),
    path("user/create/",views.create_user,name="create-user"),


    # template
    path("folder/a/",views.folder_a,name="folder-a"),
    path("folder/aa/",views.folder_aa,name="folder--a"),
    path("folder/b/",views.folderb,name="folder-b"),
    path("folder/b1/",views.folderb1,name="folder-b1"),
    # customer
    path("customer/list/",views.customer_list,name="customer-list"),
    path("customer/detail/<int:pk>/",views.customer_detail,name="customer-detail"),
    path("customer/create/",views.create_customer,name="customer-create"),
    path("customer/create/df/",views.df_customer_create_view,name="df-create-customer"),
    path("customer/update/<int:pk>/df/",views.df_customer_update_view,name="df-update-customer"),
    path("signup/",views.signup,name="sign-up"),
    path("login/",views.user_login,name="login"),
    # vehilcle
    path("create/vehicle/",views.create_vehicle,name="create-vehicle"),

    # generic views
    path("generic/view/", generic_views.MyView.as_view(), name="my-view"),
    path("generic/template/view/",generic_views.TemplateView.as_view(), name="template-view"),
    path("generic/list/view/",generic_views.CustomerListView.as_view(), name="list-view"),
    path("generic/detail/<int:pk>/view/",generic_views.CustomerDetailView.as_view(), name="detail-view"),
    path("generic/form/view/",generic_views.VehicleFormView.as_view(), name="form-view"),
    path("generic/create/view/",generic_views.VehicleCreateView.as_view(), name="create-view"),
    path("generic/update/<int:pk>/view/",generic_views.VehicalUpdateView.as_view(), name="update-view"),

    # email
    path("email/list/",views.email_list,name="email-list"),
    path("email/detail/<int:pk>/",views.email_list,name="email-detail"),
    path("email/create/",views.email_create,name="email-create")
]
# Api View
from rest_framework.urlpatterns import format_suffix_patterns
from . import api
urlpatterns += [
    path('api/customer/', api.CustomerList.as_view()),
    path('api/customer/<int:pk>/', api.CustomerDetail.as_view()),
    path('api/firstclass/',api.Firstclasslist.as_view()),
    path('api/firstclass/<int:pk>/',api.Firstclasslist.as_view()),

]

