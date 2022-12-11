from tabnanny import verbose
from django.urls import path,include
from . import views
urlpatterns = [
   path("",views.IndexPage, name="index"),
   path("register",views.registerPage, name="register"),
   path("registerUser",views.RegisterUser, name="registerUser"),
   path("otpPage",views.otpPage, name="otpPage"),
   path("otpVerification",views.otpVerify, name="otpVerify"),
   path("pagelogin",views.loginPage,name="pagelogin"),
   path("loginuser",views.loginUser,name="login"),
   path("profile/<int:pk>",views.profilePage,name="profilepage"),
   path('updateProfile/<int:pk>',views.updateProfile,name="updateProfile"),
   path('candidatejoblistpage/',views.candidateJobListPage,name="candidatejoblistpage"),
   path("applypage/<int:pk>",views.applyPage,name="applypage"),
   path("applyjob/<int:pk>",views.applyjob,name="applyjob"),
   

   # ^^^^^^^^^^^^^^^^company side^^^^^^^^^^^
   path("companyindex/",views.companyIndex,name="companyindex"),
   path("companyprofile/<int:pk>",views.companyProfile,name="companyprofile"),
   path("companyprofileUpdate/<int:pk>",views.companyProfileUpdate,name="companyprofileupdate"),
   path("jobpostpage/",views.jobpostpage,name="jobpostpage"),
   path("jobpost/<int:pk>",views.jobPost,name="jobdetails"),
   path("companylogout/",views.companylogout,name="companylogout"),
   path("postedjobtable/",views.postedJobTale,name="postedjobtable"),
   path("appliedcandidates/",views.appliedCandidates,name="appliedcandidates"),

   
# ^^^^^^^^^^^^^^^^^^ Admin Side ^^^^^^^^^^^^^^^^^^^^^^^^ 
path("adminloginpage/",views.AdminLoginPage,name="adminloginpage"),
path("adminlogin",views.AdminLogin,name="adminlogin"),
path("adminindex/",views.adminIndex,name="adminindex"),
path("adminuserlist",views.adminUserlist,name="adminuserlist"),
path("admincompanylist",views.adminCompanylist,name="admincompanylist"),
path("userdelete/<int:pk>",views.userDelete,name="userdelete"),
path("verifycompanypage/<int:pk>",views.verifyCompanyPage,name="verifycompanypage"),
path("verifycompany/<int:pk>",views.verifyCompany,name="verifycompany"),


   
]