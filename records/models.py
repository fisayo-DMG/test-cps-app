from django.db import models
from django.utils import timezone
import datetime

class Student(models.Model):
	CRECHE = 'Creche'
	PLAYGROUP_1 = 'PG1'
	PLAYGROUP_2 = 'PG2'
	KINDERGARTEN_1 = 'KG1'
	KINDERGARTEN_2 = 'KG2'
	GRADE_K = 'GK'
	GRADE_1 = 'G1'
	GRADE_2 = 'G2'
	GRADE_3 = 'G3'
	GRADE_4 = 'G4'
	GRADE_5 = 'Grade 5'
	SCHOOL_CLASS_CHOICES = (
		(CRECHE, 'Creche'),
		(PLAYGROUP_1, 'Playgroup 1'),
		(PLAYGROUP_2, 'Playgroup 2'),
		(KINDERGARTEN_1, 'Kindergarten 1'),
		(KINDERGARTEN_2, 'Kindergarten 2'),
		(GRADE_K, 'Grade K'),
		(GRADE_1, 'Grade 1'),
		(GRADE_2, 'Grade 2'),
		(GRADE_3, 'Grade 3'),
		(GRADE_4, 'Grade 4'),
		(GRADE_5, 'Grade 5'),
		)
	school_class = models.CharField(
		max_length=3,
		choices=SCHOOL_CLASS_CHOICES,
		)

	def in_kindergarten(self):
		return self.school_class in (self.KINDERGARTEN_1, KINDERGARTEN_2)

	MALE = 'M'
	FEMALE = 'F'
	
	SEX_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		)
	sex = models.CharField(
		max_length=1,
		choices=SEX_CHOICES,
		default=MALE,
		)
	surname = models.CharField(max_length=20, blank=False)
	other_names = models.CharField(max_length=20)
	father_phone = models.CharField(max_length=14, blank=True)
	mother_phone = models.CharField(max_length=14, blank=True)
	date_of_birth = models.DateField(default=datetime.date.today, 
		blank=False, null=True
		)
	age = models.IntegerField(null=True, blank=True)

	def save(self, *args, **kwargs):
		#self.age = (datetime.date.today() - self.date_of_birth).days
		age_calc = (datetime.date.today() - self.date_of_birth).days
		self.age = int(age_calc / 365.2425)
		super(Student, self).save(*args, **kwargs)

	#age_figure = int(datetime.date.today() - date_of_birth)
	#age = models.IntegerField(age_figure, null=True, blank=False)

	def __str__(self):
		return self.surname + " " + self.other_names

class Payment(models.Model):
	payment_date = models.DateField(default=timezone.now)
	name = models.ForeignKey(Student)
	amount = models.IntegerField()
	amount_paid = models.IntegerField(default=0)
	description = models.TextField()
	outstanding = models.IntegerField(default=0)

	def save(self, *args, **kwargs):
		self.outstanding = self.amount - self.amount_paid
		super(Payment, self).save(*args, **kwargs)
		
	def __str__(self):
		return str(self.name) + ", " + self.description

class Report(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()

	def __str__(self):
		return self.title

