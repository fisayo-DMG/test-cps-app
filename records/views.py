from django.shortcuts import render
from django.utils import timezone
from .models import Student

# Create your views here.
def post_list(request):
	students = Student.objects.order_by('date_of_birth')
	return render(request, 'records/post_list.html', {'students': students})