from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Student

# Create your views here.
def student_list(request):
	students = Student.objects.order_by('school_class')
	return render(request, 'records/student_list.html', {'students': students})

def student_detail(request, pk):
	student = get_object_or_404(Student, pk=pk)
	return render(request, 'records/student_detail.html', {'student': student})