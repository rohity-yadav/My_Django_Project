from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
#this functin will be  add and show the item
def add_show(request):
    stud = User.objects.all()
    if request.method=="POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration
    else:
        fm = StudentRegistration()  
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})


# this function will be edit buttun    
def update_data(request,id):
    if request .method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)        
    return render(request, 'enroll/update.html',{'form':fm})

#this function will delete
def delete_data(request,id):
    if request.method == 'POST':
        rk= User.objects.get(pk=id)
        rk.delete()
        return HttpResponseRedirect('/')