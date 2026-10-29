from django.shortcuts import render,redirect
from .models import Student
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from .forms import StudentForm


# Create your views here.
@login_required(login_url='signin')
def create_view(request):
    if request.method == "POST":
        form=StudentForm(data=request.POST)  #bounded form

        if form.is_valid():
            # name=form.cleaned_data['name']
            # roll_no=form.cleaned_data['roll_no']
            # marks=form.cleaned_data['marks']
            # email=form.cleaned_data['email']
            # course=form.cleaned_data['course']
            # contact=form.cleaned_data['contact']
            # address=form.cleaned_data['address']
    
            # Student.objects.create(name=name, roll_no=roll_no, marks=marks,
            # email=email, course=course, contact=contact, address=address,trainer=request.user)
            form.create(user=request.user)
            return redirect("display")
    else:
        form=StudentForm() #unbounded form

    context={
        'form':form,
        'operation':'Create'
    }
    
    return render(request , 'create.html',context)

@login_required(login_url='signin')
def display_view(request):
    students=Student.objects.filter(trainer=request.user)
    print(students)

    context={
        "students" : students
    }
    return render(request,'display.html',context)

@login_required(login_url='signin')
def update_view(request,student_id):
    context={}
    try:
        student=Student.objects.get(id=student_id,trainer=request.user)
        context['student']=student

    except Student.DoesNotExist:
        context["id"]=student_id
        return render(request,'error.html',context)

    if request.method == "POST":
        form=StudentForm(data=request.POST,instance=student)  #bounded form
    
        if form.is_valid():
            # name=form.cleaned_data['name']
            # roll_no=form.cleaned_data['roll_no']
            # marks=form.cleaned_data['marks']
            # email=form.cleaned_data['email']
            # course=form.cleaned_data['course']
            # contact=form.cleaned_data['contact']
            # address=form.cleaned_data['address']

            # student.name=name
            # student.roll_no=roll_no
            # student.marks=marks
            # student.email=email
            # student.course=course
            # student.contact=contact
            # student.address=address
            # student.save()
            
            # form.update(student)
            form.save() # this automatically call update() method
            return redirect('display')
    else:
        existing_data={
            'name':student.name,
            'roll_no':student.roll_no,
            'marks':student.marks,
            'email':student.email,
            'course': student.course,
            'contact':student.contact,
            'address':student.address
        }

        form= StudentForm(initial=existing_data)

    context={
        'form':form,
        'operation':'Update'
    }
    return render(request,'update.html',context)


@login_required(login_url='signin')
def delete_view(request,student_id):
    context={}
    try:
        student=Student.objects.get(id=student_id,trainer=request.user)
        context['student']=student
    except Student.DoesNotExist:
        context['id']=student_id
        return render(request,'error.html',context)

    if request.method=="POST":
        student.delete()
        return redirect('display')

    return render(request,'delete.html',context)
