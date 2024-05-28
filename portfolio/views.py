from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

correct = 0
attempted = 0


# Create your views here.

def portfolio(request):
    return render(request,'index.html')

@login_required(login_url='/login_page/')
def details(request):
    if request.method == "POST":
        data = request.POST

        id = data.get('id')
        name = data.get('name')
        phone = data.get('phone')
        class_name = data.get('class_name')
        fee_due = 1000-int(data.get('fee_due')) 
        school = data.get('school')
        department = data.get('user_type')

        depart = Department.objects.get(name = department)


        Details.objects.create(
            id = id,
            name = name,
            phone = phone,
            class_name= class_name,
            fee_due = fee_due,
            school = school,
            department = depart,
        )
        return redirect('/details/')
    queryset = Details.objects.all().order_by('id')       #by using .order_by('field_name') we can sort the values

    # for search 
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search')) # by using __icontains we can get the records which contains the search
    if request.GET.get('class_no'):
        queryset = queryset.filter(class_name__exact = request.GET.get('class_no')) #by using __exact we can get the records which exactly equal to the search
    if request.GET.get('id'):
        queryset = queryset.filter(id__icontains = request.GET.get('id'))

    context={'details' : queryset}
    return render(request,'details.html',context)

def update_details(request,id):
    queryset = Details.objects.get(id=id)
    context = {'details':queryset}
    x = Details.objects.get(id=id).fee_due


    if request.method == "POST":
        data = request.POST

        name = data.get('name')
        phone = data.get('phone')
        class_name = data.get('class_name')
        fee_due =(x-int(data.get('fee_due')))
        school = data.get('school')

        queryset.name = name
        queryset.phone = phone
        queryset.class_name = class_name
        queryset.fee_due =fee_due
        queryset.school = school

        queryset.save()

        return redirect("/details/")

    return render(request,'update.html',context)



def delete_details(request,id):

    queryset1 = Details.objects.get(id = id)
    queryset1.delete()

    return redirect('/details/')

#def search_details(request):
 #   if request.method == "POST":
  #      data = request.POST
   #     name = data.get('search')
       # queryset = Details.objects.all()

       # for details in queryset:
       #     if name == details.name:
        #        context = {'details':details}
    #    quereyset = Details.objects.filter(name__icontains=name)
#
 #       context = {'details':quereyset}
  #      return redirect('details.html')
   # return render(request,'details.html',context)    

#def register(request):
#    if request.method == "POST":
#        data = request.POST
#        first_name = data.get('first_name')
#        last_name = data.get('last_name')
#        username = data.get('username')
#        password = data.get('password')

#        user = User.objects.filter(username = username)
#        if user.exists():
#            messages.info(request,"User already exits")
#        else:
#            user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username)
 #           user.set_password(password)
  #          user.save()
   #         messages.info(request,"Account created succesfuly")

 #   return render(request,'register.html')

def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username):
            messages.error(request,'Invalid Username')
            return redirect('/login_page/')
        user = authenticate(username = username , password = password)

        #if user is None:
         #   messages.error(request,'Inavlid Username or Password')
        #else:
         #   login(request,user)
          #  return redirect('/details/')
        if user:
            profiles = Profile.objects.filter(user__username=username)
            for profile in profiles:
                if profile.user_type == 'teacher' or 'admin':
                    login(request, user)
                    return redirect('/details/')
            messages.error(request, 'Invalid Username or Password (User Type)')
        else:
            messages.error(request, 'Invalid Username or Password')

    return render(request, 'login.html')

def apply(request):
    return render (request,'apply.html')

def dashboard(request):
    return render(request,"dashboard.html")


def test(request):
    if request.method == "POST":
        data = request.POST
        question = data.get('question')
        option1 = data.get('option1')
        option2 = data.get('option2')
        option3 = data.get('option3')
        option4 = data.get('option4')
        answer = data.get('answer')


        Questions.objects.create(
            question = question,
            option1 = option1,
            option2 = option2,
            option3 = option3,
            option4 = option4,
            answer = answer,
        )
        messages.info(request,'Question uploded')
        return redirect('/test/')


    return render(request,"question.html")
@login_required(login_url='/student_login/')
def exam(request):
    queryset = Questions.objects.all()
    print(request.user.username)
    context = {'answers': queryset}
    #x = queryset.filter(answer = 'answer')
    x =  request.GET.get('answer')
    y = queryset.filter(answer = x)
    print(x)
    print(y)
    queryset2 = Marks.objects.all()
    z = queryset2.get(std_id = request.user.username)
    print(z)
    if y:
        z.count = z.count + 2
        z.save()
        print("saved")
    return render(request, 'exam.html', context)

def marks(request):
    queryset = Marks.objects.all()
    x = queryset.get(std_id = request.user.username)
    count = x.count
    x.count = 0
    x.save()
    return render (request,'marks.html',{'count':count})

def student_login(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username=username):
            messages.error(request,'Invalid Username')
            return redirect('/login_page/')
        user = authenticate(username = username , password = password)

        if user:
            profiles = Profile.objects.filter(user__username=username)
            for profile in profiles:
                if profile.user_type == 'student' or 'admin':
                    login(request, user)
                    return redirect('/exam/')
            messages.error(request, 'Invalid Username or Password (User Type)')
        else:
            messages.error(request, 'Invalid Username or Password')

    return render(request, 'login.html')








