from django.shortcuts import render,redirect
from . import models
from first_app.forms import StudentForm
from django.contrib import messages
# Create your views here.

def home(request):
    students = models.Student.objects.all()
    print(students)
    return render(request, 'home.html',{'data':students})
def delete_user(request,id):
    students = models.Student.objects.get(pk=id)
    students.delete()
    print(students)
    return redirect('home')

def form(request):
    if request.method == 'POST':

        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form successfully submitted!')
        
    else:
        form = StudentForm()
    
    
    return render(request,'form.html',{"form": form})
