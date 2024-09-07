from django.shortcuts import render,HttpResponse,redirect
from .models import*
from django.contrib import messages
from django.contrib.auth import logout
from django.utils.decorators import decorator_from_middleware
from .middleware import NoCacheMiddleware
# Create your views here.

def index(request):
    ss=student.objects.all()
    return render(request, 'index.html', {'st': ss,"btn":"save","state":""})



def save(request):
    ss=student()

    for i in request.POST.keys():
        setattr(ss,i,request.POST[i])
    ss.save()
    if ss.id == request.POST['id']:
        messages.success(request, 'stduetn record updated successfully')
    else:
        messages.success(request, 'stduetn added successfully')

    return redirect('index')

def login(request):
    # ss=student.objects.all()
    return render(request, 'login.html',)

def register(request):
    # ss=student.objects.all()
    return render(request, 'register.html',)
def edit(request,id):
    ss = student.objects.get(pk=id)
    sss_all = student.objects.all()
    return render(request,"index.html",{"st":sss_all,"ss":ss,"btn":"update","state":"readonly"})

def delete( request,id):
    ss= student.objects.get(pk=id)
    ss.delete()
    messages.success(request, 'stduetn Deletet successfully')
    return redirect ('index')


def add_user(request):
    if request.method == 'POST':
        user = request.POST.get('User')
        email = request.POST.get('Email')
        password = request.POST.get('Pass')
        # print(Users,"--------------------------------" * 100)
        if user != "" and email != "" and password != "":
            new_user = Users(username=user, email=email,password=password)
            
            new_user.save()

            return render(request, "login.html", messages.success(request, 'succcessfully registered'))
    else:
        return HttpResponse("Invalid request method.", status=405)
    
    
def check(request):
    if request.method == 'POST':
        user = request.POST.get('User')
        password = request.POST.get('Pass')
        try:
            user_data = Users.objects.get(username=user)
        except:
            user_data = None
        if user_data == None:
            return render(request,"login.html",messages.error(request,"Username and password is not recoginazed"))
        
        if user_data.password == password:
            user_count = Users.objects.count()
            request.session["Userka"] = user
            print(request.session.get("Userka"),"_"*100)
            return render(request,"index.html",{"message":"login successfully ",'btn':"save","Users":user_count})
        else:
            return render(request,"login.html",messages.success(request, 'Incorrect Username or Password'))

            
def logout(request):
    response = redirect('login')
    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response