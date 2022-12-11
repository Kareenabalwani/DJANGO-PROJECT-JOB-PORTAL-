from webbrowser import get
from django.shortcuts import redirect, render
from .models import *
from random import randint
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")

def registerPage(request):
    return render(request,'app/register.html')  

def RegisterUser(request):
    if request.method == "POST":

        if request.POST.get('roles')=="Candidate":
            
            fname =request.POST.get('firstname')
            lname =request.POST.get('lastname')
            email =request.POST.get('email')
            role =request.POST.get('roles')
            password =request.POST.get('password')
            cpassword =request.POST.get('cpassword')

            user = UserMaster.objects.filter(email=email)
            if user:

                message = "User already exist !"
                return render(request,'app/signup.html',{'msg':message})
            else:
                if password == cpassword:

                    otp = randint(10000,99999)
                    newuser = UserMaster.objects.create(role=role,otp=otp,password=password,email=email)
                    newCandidate = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                    
                    return render(request,'app/otpverify.html',{'email':email})
        else:
            
            if request.POST.get('roles')=="Company":

                fname =request.POST.get('firstname')
                lname =request.POST.get('lastname')
                email =request.POST.get('email')
                role =request.POST.get('roles')
                password =request.POST.get('password')
                cpassword =request.POST.get('cpassword')

                user = UserMaster.objects.filter(email=email)
                if user:

                    
                    message = "Company already exist !"
                    return render(request,'app/register.html',{'msg':message})
                else:

                    if password == cpassword:

                        otp = randint(10000,99999)
                        newuser = UserMaster.objects.create(role=role,otp=otp,password=password,email=email)
                        newCandidate = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                    
                        return render(request,'app/otpverify.html',{'email':email})


                    

def loginPage(request):
    return render(request,"app/login.html")

def otpPage(request):
    return render(request,'app/otpverify.html')
         

      
def otpVerify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
    user = UserMaster.objects.get(email=email)

    if user:

        if user.otp ==otp:

            message = "otp verified successfully !"
            return render(request,'app/login.html',{'mssg':message})
        else:
            message = "Incorrect OTP:"
            return render(request,'app/otpverify.html',{'msg':message})
    else:
        return render(request,'app/register.html')


def loginUser(request):
    if request.POST['roles']=="Candidate":
        email = request.POST['email']
        password = request.POST['password']
        user = UserMaster.objects.get(email=email)
        if user:
            if password==user.password and user.role=='Candidate':
                cand = Candidate.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['role']=user.role
                request.session['firstname']=cand.firstname
                request.session['lastname']=cand.lastname
                request.session['email']=user.email
                request.session['password']=user.password
                return redirect('index')
            else:
                message = "Password Doesn't match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User Doesn't Exist"
            return render(request,"app/login.html",{'msg':message})
    else:
        if request.POST['roles']=="Company":

            email = request.POST['email']
            password = request.POST['password']
            user = UserMaster.objects.get(email=email)
            if user:
                if password==user.password and user.role=='Company':
                    com = Company.objects.get(user_id=user)
                    request.session['id']=user.id
                    request.session['company_id']=com.id
                    request.session['role']=user.role
                    request.session['firstname']=com.firstname
                    request.session['lastname']=com.lastname
                    request.session['email']=user.email
                    request.session['password']=user.password
                    return redirect('companyindex')
                else:
                    message = "Password Doesn't match"
                    return render(request,"app/login.html",{'msg':message})


                
        else:
            message = "User Doesn't Exist"
            return render(request,"app/login.html",{'msg':message})

def profilePage(request,pk):

    user =UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id = user)
    return render(request,"app/profile.html",{'user':user,'cand':can})


def updateProfile(request,pk):
    
    user = UserMaster.objects.get(pk=pk)
    if user.role == 'Candidate':
        cand = Candidate.objects.get(user_id=user)
        cand.firstname = request.POST['firstname']
        cand.lastname = request.POST['lastname']
        cand.country = request.POST['country']
        cand.state = request.POST['state']
        cand.city = request.POST['city']
        cand.contact = request.POST['phone']
        cand.dob = request.POST['dob']
        cand.exp = request.POST['exp']
        cand.edu = request.POST['qualification']
        cand.min_salary = request.POST['min_salary']
        cand.job_category = request.POST['job_category']        
        cand.website = request.POST['website']
        cand.gender = request.POST['gender']
        cand.profile_pic = request.FILES['profile_pic']
        cand.save()
        # url = f'/profilepage/{pk}' 
        #formatting url
        # write your code for redirecting the profile page mene index pe redirect kiya hai filhal
        return redirect('profilepage',pk=pk)




# ^^^^^^^^^^^^^^^^^^ Company Side ^^^^^^^^^^^^^^^^^^^^^^^^ 

def companyIndex(request):
    return render(request,"app/company/index.html")



def companyProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id= user)
    return render(request,'app/company/company_profile.html',{'user':user,'comp':comp})


def companyProfileUpdate(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role =='Company':
        comp = Company.objects.get(user_id=user)
        comp.firstname = request.POST['firstname']
        comp.lastname = request.POST['lastname']
        comp.email = request.POST['email']
        comp.contact = request.POST['contact']
        comp.website = request.POST['website']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.company_address = request.POST['company_address']
        comp.profile_pic = request.FILES['company_logo']
        comp.save()
        return redirect('companyprofile',pk=pk)


def jobpostpage(request):
    return render(request,'app/company/jobpostpage.html')

def jobPost(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress = request.POST['companyaddress']
        location = request.POST['location']
        jobdescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsibility = request.POST['responsibility']
        workmode = request.POST['workmode']
        companywebsite = request.POST['companywebsite']
        companyemail = request.POST['companyemail']
        experience = request.POST['experience']
        skills = request.POST['skills']
        salary = request.POST['salary']
        timing = request.POST['timing']
        jobs = jobDetails.objects.create(company_id=comp,jobname=jobname,companyname=companyname,companyaddress=companyaddress,location=location,jobdescription=jobdescription,qualification=qualification,responsibilities=responsibility,workmode=workmode,companywebsite=companywebsite,companyemail=companyemail,experience=experience,skills=skills,salary=salary,timing=timing)
        msg ="Job posted successfully !"
        return render(request,"app/company/jobpostpage.html",{'msg':msg})


def postedJobTale(request):
    all_jobs = jobDetails.objects.all()
    return render(request,"app/company/postedjobtable.html",{'all_jobs':all_jobs})

def candidateJobListPage(request):
    all_jobs = jobDetails.objects.all()
    return render(request,"app/jobslist.html",{'all_jobs':all_jobs})

def companylogout(request):
    del request.session['email']
    del request.session['password']
    del request.session['firstname']
    del request.session['lastname']
    del request.session['id']
    return render(request,'app/index.html')


def applyPage(request,pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = jobDetails.objects.get(pk=pk)
        return render(request,"app/apply.html",{'user':user,'cand':cand,'job':job})



def applyjob(request,pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(user_id=user)
        job = jobDetails.objects.get(pk=pk)
        cfname = request.POST['firstname']
        clname = request.POST['lastname']
        ccontact = request.POST['phone']
        cexp = request.POST['exp']
        cedu = request.POST['qualification']
        cmin_salary = request.POST['min_salary']
        cjob_category = request.POST['job_category']        
        cwebsite = request.POST['website']
        cgender = request.POST['gender']
        cresume = request.FILES['resume']
        newjob = ApplyJob.objects.create(candidate=cand,job=job,firstname=cfname,lastname=clname,contact=ccontact,min_salary=cmin_salary,edu=cedu,gender=cgender,exp=cexp,job_category=cjob_category,website=cwebsite,resume=cresume)
        msg = "Applied for job successfully !"
        return render(request,"app/apply.html",{'msg':msg})

def appliedCandidates(request):
    cid = request.session['company_id']
    all_jobs = ApplyJob.objects.all()
    return render(request,"app/company/appliedcandidates.html",{'all_jobs':all_jobs})



# ^^^^^^^^^^^^^^^^^^Admin Side ^^^^^^^^^^^^^^^^^^^^^^^^ 
def AdminLoginPage(request):
    return render(request,"app/admin/login.html")

def adminIndex(request):
    if 'adminusername' in request.session and 'adminpassword' in request.session:
        return render(request,"app/admin/index.html")
    else:
        return render(request,"app/admin/login.html")


def AdminLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == "admin" and password == "admin":
        request.session['adminusername']=username
        request.session['adminpassword'] =password
        return redirect('adminindex') 
    else:
        msg = "Username or password are Incorrect !"
        return render(request,"app/admin/login.html",{'msg':msg})


def adminUserlist(request):
    user = UserMaster.objects.filter(role= 'Candidate')
    return render(request,"app/admin/userlist.html",{'cand':user})


def adminCompanylist(request):
    company = UserMaster.objects.filter(role= 'Company')
    return render(request,"app/admin/companylist.html",{'comp':company})



def userDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect("adminuserlist")

def verifyCompanyPage(request,pk):
    comp = UserMaster.objects.get(pk=pk)
    return render(request,'app/admin/verifycompany.html',{'comp':comp})
    
def verifyCompany(request,pk):
    comp = UserMaster.objects.get(pk=pk)
    comp.is_varified = request.POST['verify']
    comp.save()
    return redirect('admincompanylist')

def companyDelete(request,pk):
    comp = UserMaster.objects.get(pk=pk)
    comp.delete()
    return redirect("admincompanylist")




