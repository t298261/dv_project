from django import forms
from .models import *



class StepOneForm(forms.ModelForm):
	class Meta: 
		model = StepOne
		fields= ("box1","box2","box3", "box4", "box5", "box6")

class StepTwoForm(forms.ModelForm):
	class Meta: 
		model = StepTwo  
		fields= ("box1","box2","box3", "box4", "box5", "box6", "box7", "box8", "box9")

class StepThreeForm(forms.ModelForm):
	class Meta: 
		model = StepThree  
		fields= ("box1","box2","box3", "box4", "box5", "box6", "box7", "box8")

class StepFourForm(forms.ModelForm):
	class Meta: 
		model = StepFour
		fields= ("box1","box2","box3", "box4", "box5", "box6", "box7")

class StepFiveForm(forms.ModelForm):
	class Meta: 
		model = StepFive
		fields= ("box1","box2","box3", "box4", "box5")

class StepSixForm(forms.ModelForm):
	class Meta: 
		model = StepSix
		fields= ("box1","box2","box3")

class StepSevenForm(forms.ModelForm):
	class Meta: 
		model = StepSeven
		fields= ("box1","box2","box3", "box4", "box5", "box6", "box7")

class StepEightForm(forms.ModelForm):
	class Meta: 
		model = StepEight
		fields= ("box1","box2","box3", "box4", "box5", "box6", "box7")


