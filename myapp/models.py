from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm



class StepOne(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	update = "Update"
	box1 = models.CharField(max_length=100, null=True)
	box2 = models.CharField(max_length=100, null=True)
	box3 = models.CharField(max_length=100, null=True)
	box4 = models.CharField(max_length=100, null=True)
	box5 = models.CharField(max_length=100, null=True)
	box6 = models.CharField(max_length=100, null=True)
	
	def __str__(self):
		return self.update

class StepTwo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	update = "Update"
	box1 = models.CharField(max_length=100, null=True)
	box2 = models.CharField(max_length=100, null=True)
	box3 = models.CharField(max_length=100, null=True)
	box4 = models.CharField(max_length=100, null=True)
	box5 = models.CharField(max_length=100, null=True)
	box6 = models.CharField(max_length=100, null=True)
	box7 = models.CharField(max_length=100, null=True)
	box8 = models.CharField(max_length=100, null=True)
	box9 = models.CharField(max_length=100, null=True)
	
	def __str__(self):
		return self.update

class StepThree(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	update = "Update"
	box1 = models.CharField(max_length=100, null=True)
	box2 = models.CharField(max_length=100, null=True)
	box3 = models.CharField(max_length=100, null=True)
	box4 = models.CharField(max_length=100, null=True)
	box5 = models.CharField(max_length=100, null=True)
	box6 = models.CharField(max_length=100, null=True)
	box7 = models.CharField(max_length=100, null=True)
	box8 = models.CharField(max_length=100, null=True)
	
	def __str__(self):
		return self.update


class StepFour(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	update = "Update"
	box1 = models.CharField(max_length=100, null=True)
	box2 = models.CharField(max_length=100, null=True)
	box3 = models.CharField(max_length=100, null=True)
	box4 = models.CharField(max_length=100, null=True)
	box5 = models.CharField(max_length=100, null=True)
	box6 = models.CharField(max_length=100, null=True)
	box7 = models.CharField(max_length=100, null=True)
	
	def __str__(self):
		return self.update


class StepFive(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	update = "Update"
	box1 = models.CharField(max_length=100, null=True)
	box2 = models.CharField(max_length=100, null=True)
	box3 = models.CharField(max_length=100, null=True)
	box4 = models.CharField(max_length=100, null=True)
	box5 = models.CharField(max_length=100, null=True)
	
	def __str__(self):
		return self.update

class StepSix(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	name ='Form 6 Name'
	box1 = models.CharField(max_length=100, null=True)
	box2 = models.CharField(max_length=100, null=True)
	box3 = models.CharField(max_length=100, null=True)
	
	def __str__(self):
		return self.name

class StepSeven(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	name ='Form 7 Name'
	box1 = models.CharField(max_length=100, null=True)
	box2 = models.CharField(max_length=100, null=True)
	box3 = models.CharField(max_length=100, null=True)
	box4 = models.CharField(max_length=100, null=True)
	box5 = models.CharField(max_length=100, null=True)
	box6 = models.CharField(max_length=100, null=True)
	box7 = models.CharField(max_length=100, null=True)

	
	def __str__(self):
		return self.name

class StepEight(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	name ='Form 8 Name'
	box1 = models.CharField(max_length=100, null=True)
	box2 = models.CharField(max_length=100, null=True)
	box3 = models.CharField(max_length=100, null=True)
	box4 = models.CharField(max_length=100, null=True)
	box5 = models.CharField(max_length=100, null=True)
	box6 = models.CharField(max_length=100, null=True)
	box7 = models.CharField(max_length=100, null=True)
	
	
	def __str__(self):
		return self.name



# class CreateUserForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ['username', 'password1', 'password2']



