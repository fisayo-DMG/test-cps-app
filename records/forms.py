from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('school_class', 'sex', 'surname', 'other_names',
			'father_phone', 'mother_phone', 'date_of_birth', 'age')