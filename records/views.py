from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Student
from .forms import StudentForm
from django.shortcuts import redirect

# Create your views here.
def student_list(request):
	students = Student.objects.order_by('school_class')
	return render(request, 'records/student_list.html', {'students': students})

def student_detail(request, pk):
	student = get_object_or_404(Student, pk=pk)
	return render(request, 'records/student_detail.html', {'student': student})

def student_new(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			student = form.save()
			return redirect('student_detail', pk=student.pk)
	else:
		form = StudentForm()
	return render(request, 'records/student_edit.html', {'form': form})

def student_edit(request, pk):
	student = get_object_or_404(Student, pk=pk)
	if request.method == "POST":
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			student = form.save()
			return redirect('student_detail', pk=student.pk)
	else:
		form = StudentForm(instance=student)
	return render(request, 'records/student_edit.html', {'form': form})