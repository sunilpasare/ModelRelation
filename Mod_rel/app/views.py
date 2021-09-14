from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Department, Student,Lecture
from .forms import StudentModel,LectureModel


def Student_register_view(request):
    form=StudentModel()
    if request.method=='POST':
        form=StudentModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stud')
    template_name='StudentRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def Lecturer_register_view(request):
    form=LectureModel()
    if request.method=='POST':
        form=LectureModel(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecd')
    template_name='LectureRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def Student_list_view(request):
    stu=Student.objects.all()
    template_name='StudentShow.html'
    context={'stu':stu}
    for i in stu:
        print(str(i.Department))
    return render(request,template_name,context)
    

def Lecturer_list_view(request):
    Lec=Lecture.objects.all()
    template_name='LecturerShow.html'
    context={'Lec':Lec}
    for i in Lec:
        print(str(i.Department))
    return render(request,template_name,context)

def Student_update_view(request,update):
    ord=Student.objects.get(id=update)
    form=StudentModel(instance=ord)
    if request.method=='POST':
        form=StudentModel(request.POST,instance=ord)
        if form.is_valid():
            form.save()
            return redirect('stud')
    template_name='StudentRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def Student_delete_view(request,delet):
    dal=Student.objects.get(id=delet)
    dal.delete()
    return redirect('stud')

def Lecture_update_view(request,update):
    ord=Lecture.objects.get(id=update)
    form=LectureModel(instance=ord)
    if request.method=='POST':
        form=LectureModel(request.POST,instance=ord)
        if form.is_valid():
            form.save()
            return redirect('lecd')
    template_name='LectureRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def Lecture_delete_view(request,delet):
    dal=Lecture.objects.get(id=delet)
    dal.delete()
    return redirect('lecd')



def Homeview(request):
    if request.method=='POST':
        search=request.POST.get('search')
        stu=Student.objects.filter(sname__contains=search)
        lec=Lecture.objects.filter(lname__contains=search)
        dep=Department.objects.filter(dname__contains=search).first()
        print(dep)
        if dep is not None:
            stu_dep=Student.objects.filter(Department_id=dep)
            lec_dep=Lecture.objects.filter(Department=dep.id)
            template_name='Home.html'
            context={'stu_dep':stu_dep,'lec_dep':lec_dep,'dep':dep}
            return render(request,template_name,context)
        template_name='Home.html'
        context={'stu':stu,'lec':lec}
        return render(request,template_name,context)
    template_name='Home.html'
    context={'ord':'ord'}
    return render(request,template_name,context)









