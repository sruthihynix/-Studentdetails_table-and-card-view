from django.shortcuts import render,redirect
from student_app.models import Student_Details


# Create your views here.
def add_student(request):
    if request.method == 'POST':
        student = Student_Details()

        student.student_id = request.POST.get('student_id')
        student.student_name = request.POST.get('student_name')
        student.student_class = request.POST.get('student_class')
        student.student_contact = request.POST.get('student_contact')
        student.student_image = request.FILES.get('student_image')
        print(student.student_id)
        student.save()
        return redirect('/HomePage')
    return render(request,"add_student.html")

def HomePage(request):
    print("hai home page")
    student = Student_Details.objects.all()
    return render(request,'Home.html',{'data' : student}) # data is the dictionary key and in student the values
                                                          #

def CardView(request):
    students = Student_Details.objects.all()
    return render(request, 'cards.html', {'data': students})