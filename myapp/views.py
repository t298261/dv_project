from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt











### Connection from Github to PythonWnyhere
# @csrf_exempt
# def git_pythonanywhere(request):
#     if request.method == "POST":

#         repo = git.Repo("wepwawet.pythonanywhere.com/") 
		
#         origin = repo.remotes.origin

#         origin.pull()

#         return HttpResponse("Updated code on PythonAnywhere")
#     else:
#         return HttpResponse("Couldn't update the code on PythonAnywhere")



###PDF Features###








###General###


def base(request):
	"""css, navbar and block content to include on every page"""
	return render(request, 'base.html')

def userHomepage(request):
	"""Gets objects to display on user homepage and redirects user to user homepage"""
	return render(request, 'index.html')

def form_view_error(request):
	""" Display redirect when no form has been completed"""
	return render(request, 'redirect_userhome.html')

def form_one_page(request):
	form1 = StepOne.objects.filter(user=request.user)
	step1 = StepOne.objects.filter(user=request.user) # if you want to mess with messages.
	#form1 = StepOne.objects.all() # this would get the last form submitted by any user being passed.
	context = { 'form1': form1,
				'step1': step1
	}
	"""Takes User to Step1 Page"""
	return render(request, 'form_one_page.html', context)

def form_two_page(request):
	"""Takes User to Step2 Page"""
	form2 = StepTwo.objects.filter(user=request.user)
	context = { 'form2': form2,
	}
	return render(request, 'form_two_page.html', context)

def form_three_page(request):
	"""Takes User to Step3 Page"""
	form3 = StepThree.objects.filter(user=request.user)
	context = { 'form3': form3,
	}
	return render(request, 'form_three_page.html', context)

def form_four_page(request):
	"""Takes User to Step4 Page"""
	form4 = StepFour.objects.filter(user=request.user)
	context = { 'form4': form4,
	}
	return render(request, 'form_four_page.html', context)

def form_five_page(request):
	"""Takes User to Step5 Page"""
	form5 = StepFive.objects.filter(user=request.user)
	context = { 'form5': form5,
	}
	return render(request, 'form_five_page.html', context)

def form_six_page(request):
	"""Takes User to Step6 Page"""
	form6 = StepSix.objects.filter(user=request.user)
	context = { 'form6': form6,
	}
	return render(request, 'form_six_page.html', context)

def form_seven_page(request):
	"""Takes User to Step7 Page"""
	form7 = StepSeven.objects.filter(user=request.user)
	context = { 'form7': form7,
	}
	return render(request, 'form_seven_page.html', context)

def form_eight_page(request):
	"""Takes User to Step8 Page"""
	form8 = StepEight.objects.filter(user=request.user)
	context = { 'form8': form8,
	}
	return render(request, 'form_eight_page.html', context)


###########Users##############

def register_user(request):
	form = UserCreationForm()
	if request.method == 'POST': #if someone has filled out a form do something.
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']
			user = authenticate(username=username, password=password) #authenticate user
			login(request, user)  #log user in
			messages.success(request, 'Registration Successful')
			return redirect('user-homepage')
		else:
			messages.success(request, 'Already Registered, please log in.')
	return render(request, 'register.html', {'form': form} )


def shellTesting(request):
	thing = StepOne.objects.get(user=request.user)
	return render(request, 'shell_test.html', {'thing': thing})


def welcome(request):
	return render(request, 'welcome.html')


def loginPage(request):
	if request.method == "POST": #The user entered the info and logged in.
		username = request.POST.get('username') #this is sent from the front end through the login.html.
		password = request.POST.get('password')
		try:
			user= User.objects.get(username=username)
		except:
			messages.error(request, "User does not exist.")
		user = authenticate(request, username=username, password=password) #if get was successful authenticate user.
		if user is not None: #if we got a user
			login(request, user) #will add the session in the database and browser.
			return redirect('user-homepage')
		else:
			messages.error(request, "Username or password does not exist.")
	context = {}
	return render(request, 'login_registration.html', context)


def logoutUser(request):
	logout(request) # deletes the token/user session
	return redirect('welcome')

###########Form1##############

@login_required(login_url='login_user')
def Step1_Form_Completion(request):
	"""Generates link for user to fill out form"""
	form = StepOneForm                #Assign the form to the variable in the function.
	if request.method == 'POST':     # if method or form is requested then POST or send data to this function. If someone is loggded in . . 
		try:
			form = StepOneForm(request.POST) #the method is form and it is to be posted.
			if form.is_valid():             #if the form is django's definiton for 'valid' then save it and redirect the user home.
				form.instance.user = request.user
				form.save()
				return redirect('step1_page')
		except:
			messages.success(request, 'Cannot resubmit. Please use "edit" instead.')
			return redirect('user-homepage')

	return render(request, 'form.html', {'form':form} ) # return  this function to the form.html page and let it use form as s variable and call it's attributes (form.box1)


@login_required(login_url='login_user')  #sends user back to login page if they try to go to a view form.
def Step1_Form_View(request, step_one):
	"""View for user to see completed form"""
	step1 = StepOne.objects.filter(user=request.user) # user can only view theire form. request user and filter the objects/forms for there step oneform.
	return render(request,'form_view.html',{'step1': step1})

@login_required
def editpost(request, step_one):
	"""Form1 Edit post function"""
	step1 = StepOne.objects.filter(user=request.user.id) #Gets user id and finds if they have a StepOne form.
	step_one = StepOne.objects.get(pk=step_one) #Gets passed the form id by logged in user. See function form_one_page to see how it's passing query string.
	form = StepOneForm(instance=step_one)
	if request.method == 'POST':
		form = StepOneForm(request.POST, instance=step_one)
		if form.is_valid():
			form.save()
			return redirect('user-homepage')
	return render(request,'update_form.html', {"form": form, "step1": step1})

@login_required(login_url='login_user')
def Step1_Form_Delete(request, step_one): # WORKS! Just not the error messagse because there is no stepone.
	step1 = StepOne.objects.filter(user=request.user.id)  # this doesn't work. kept here as a note.
	form = StepOne.objects.get(pk=step_one)
	if request.method == "POST":
		form.delete()
		return redirect("user-homepage")
	context = {'form': form, "step1": step1}
	return render(request, 'delete_form1.html', context)

###########Form2##############

@login_required(login_url='login_user')
def Step2_Form_Completion(request):
	"""Generates link for user to fill out form"""
	form = StepTwoForm                
	if request.method == 'POST': 
		try:
			form = StepTwoForm(request.POST) 
			if form.is_valid():         
				form.instance.user = request.user
				form.save()
				return redirect('step2_page')
		except:
			messages.success(request, 'Cannot resubmit. Please use "edit" instead.')
			return redirect('user-homepage')
	return render(request, 'form2.html', {'form':form} )


@login_required(login_url='login_user')  
def Step2_Form_View(request):
	"""View for user to see completed form"""
	step2 = StepTwo.objects.filter(user=request.user)
	return render(request, 'form_view2.html', {"step2": step2} )


@login_required
def editpost2(request, step_two ):
	"""Form1 Edit post function"""
	step2 = StepTwo.objects.filter(user=request.user)
	step_two = StepTwo.objects.get(pk=step_two)
	form2 = StepTwoForm(instance=step_two)
	if request.method == 'POST':
		form2 = StepTwoForm(request.POST, instance=step_two)
		if form2.is_valid():
			form2.save()
			return redirect('user-homepage')
	return render(request,'update_form2.html', {"form2": form2, "step2": step2})

@login_required(login_url='login_user')
def Step2_Form_Delete(request, step_two):
    form = StepTwo.objects.get(pk=step_two)
    if request.method == "POST":
    	form.delete()
    	return redirect("user-homepage")
    context = {'form': form}
    return render(request, 'delete_form2.html', context)


###########Form3##############


@login_required(login_url='login_user')
def Step3_Form_Completion(request):
	"""Generates link for user to fill out form"""
	form = StepThreeForm                
	if request.method == 'POST': 
		try:
			form = StepThreeForm(request.POST) 
			if form.is_valid():         
				form.instance.user = request.user
				form.save()
				return redirect('step3_page')
		except:
			messages.success(request, 'Cannot resubmit. Please use "edit" instead.')
			return redirect('user-homepage')
	return render(request, 'form3.html', {'form':form} )


@login_required(login_url='login_user')  
def Step3_Form_View(request):
	"""View for user to see completed form"""
	step3 = StepThree.objects.filter(user=request.user)
	return render(request, 'form_view3.html', {"step3": step3} )

@login_required
def editpost3(request, step_three):
	"""Form3 Edit post function"""
	step3 = StepThree.objects.filter(user=request.user)
	step_three = StepThree.objects.get(pk=step_three) #Needs to be a form completed by any user for this to work.
	form3 = StepThreeForm(instance=step_three)
	if request.method == 'POST':
		form3 = StepThreeForm(request.POST, instance=step_three)
		if form3.is_valid():
			form3.save()
			return redirect('user-homepage')
	return render(request,'update_form3.html', {"form3": form3, "step3": step3})

@login_required(login_url='login_user')
def Step3_Form_Delete(request, step_three):
    form = StepThree.objects.get(pk=step_three)
    if request.method == "POST":
    	form.delete()
    	return redirect("user-homepage")
    context = {'form': form}
    return render(request, 'delete_form3.html', context)


###########Form4##############

@login_required(login_url='login_user')
def Step4_Form_Completion(request):
	"""Generates link for user to fill out form"""
	form = StepFourForm                #Assign the form to the variable in the function.
	if request.method == 'POST':     # if method or form is requested then POST or send data to this function. If someone is loggded in . . 
		try:
			form = StepFourForm(request.POST) #the method is form and it is to be posted.
			if form.is_valid():             #if the form is django's definiton for 'valid' then save it and redirect the user home.
				form.instance.user = request.user
				form.save()
				return redirect('step4_page')
		except:
			messages.success(request, 'Cannot resubmit. Please use "edit" instead.')
			return redirect('user-homepage')

	return render(request, 'form4.html', {'form':form} ) # return  this function to the form.html page and let it use form as s variable and call it's attributes (form.box1)


@login_required(login_url='login_user')  #sends user back to login page if they try to go to a view form. From my tests you don't need the login url= part.
def Step4_Form_View(request):
	"""View for user to see completed form"""
	step4 = StepFour.objects.filter(user=request.user) #user can only view there form. request user and filter the objects/forms for there step oneform.
	return render(request,'form_view4.html',{'step4': step4})

@login_required(login_url='login_user')
def editpost4(request, step_four ):
	"""Form1 Edit post function"""
	step4 = StepFour.objects.filter(user=request.user)
	step_four = StepFour.objects.get(pk=step_four)
	form4 = StepFourForm(instance=step_four)
	if request.method == 'POST':
		form4 = StepFourForm(request.POST, instance=step_four)
		if form4.is_valid():
			form4.save()
			return redirect('user-homepage')
		else:
			return HttpResponse("Please complete a form first")

	return render(request,'update_form4.html', {"form4": form4, 'step4': step4})

@login_required(login_url='login_user')
def Step4_Form_Delete(request, step_four):
    form = StepFour.objects.get(pk=step_four)
    if request.method == "POST":
    	form.delete()
    	return redirect("user-homepage")
    context = {'form': form}
    return render(request, 'delete_form4.html', context)


###########Form5##############

@login_required(login_url='login_user')
def Step5_Form_Completion(request):
	"""Generates link for user to fill out form"""
	form = StepFiveForm                #Assign the form to the variable in the function.
	if request.method == 'POST':     # if method or form is requested then POST or send data to this function. If someone is loggded in . . 
		try:
			form = StepFiveForm(request.POST) #the method is form and it is to be posted.
			if form.is_valid():             #if the form is django's definiton for 'valid' then save it and redirect the user home.
				form.instance.user = request.user
				form.save()
				return redirect('step5_page')
		except:
			messages.success(request, 'Cannot resubmit. Please use "edit" instead.')
			return redirect('user-homepage')

	return render(request, 'form5.html', {'form':form} ) # return  this function to the form.html page and let it use form as s variable and call it's attributes (form.box1)


@login_required(login_url='login_user')  #sends user back to login page if they try to go to a view form in the address bar that isn't their's.
def Step5_Form_View(request):
	"""View for user to see completed form"""
	step5 = StepFive.objects.filter(user=request.user) #user can only view there form. request user and filter the objects/forms for there step oneform.
	return render(request,'form_view5.html',{'step5': step5})

@login_required
def editpost5(request, step_five ):
	"""Form1 Edit post function"""
	step_five = StepFive.objects.get(pk=step_five)
	form5 = StepFiveForm(instance=step_five)
	step5 = StepFive.objects.filter(user=request.user)
	if request.method == 'POST':
		form5 = StepFiveForm(request.POST, instance=step_five)
		if form5.is_valid():
			form5.save()
			return redirect('user-homepage')
	return render(request,'update_form5.html', {"form5": form5, 'step5': step5})

@login_required(login_url='login_user')
def Step5_Form_Delete(request, step_five):
    form = StepFive.objects.get(pk=step_five)
    if request.method == "POST":
    	form.delete()
    	return redirect("user-homepage")
    context = {'form': form}
    return render(request, 'delete_form5.html', context)

###########Form6##############


@login_required(login_url='login_user')
def Step6_Form_Completion(request):
	"""Generates link for user to fill out form"""
	form = StepSixForm                #Assign the form to the variable in the function.
	if request.method == 'POST':     # if method or form is requested then POST or send data to this function. If someone is loggded in . . 
		try:
			form = StepSixForm(request.POST) #the method is form and it is to be posted.
			if form.is_valid():             #if the form is django's definiton for 'valid' then save it and redirect the user home.
				form.instance.user = request.user
				form.save()
				return redirect('step6_page')
		except:
			messages.success(request, 'Cannot resubmit. Please use "edit" instead.')
			return redirect('user-homepage')
	return render(request, 'form6.html', {'form':form} ) # return  this function to the form.html page and let it use form as s variable and call it's attributes (form.box1)


@login_required(login_url='login_user')  #sends user back to login page if they try to go to a view form in the address bar that isn't their's.
def Step6_Form_View(request):
	"""View for user to see completed form"""
	step6 = StepSix.objects.filter(user=request.user) #user can only view there form. request user and filter the objects/forms for there step oneform.
	return render(request,'form_view6.html',{'step6': step6})

@login_required
def editpost6(request, step_six ):
	"""Form1 Edit post function"""
	step_six = StepSix.objects.get(pk=step_six)
	form6 = StepSixForm(instance=step_six)
	step6 = StepSix.objects.filter(user=request.user)
	if request.method == 'POST':
		form6 = StepSixForm(request.POST, instance=step_six)
		if form6.is_valid():
			form6.save()
			return redirect('user-homepage')
	return render(request,'update_form6.html', {'form6': form6, 'step6': step6})

@login_required(login_url='login_user')
def Step6_Form_Delete(request, step_six):
    form = StepSix.objects.get(pk=step_six)
    if request.method == "POST":
    	form.delete()
    	return redirect("user-homepage")
    context = {'form': form}
    return render(request, 'delete_form6.html', context)

    ###########Form7##############


@login_required(login_url='login_user')
def Step7_Form_Completion(request):
	"""Generates link for user to fill out form"""
	form = StepSevenForm                #Assign the form to the variable in the function.
	if request.method == 'POST':     # if method or form is requested then POST or send data to this function. If someone is loggded in . . 
		try:
			form = StepSevenForm(request.POST) #the method is form and it is to be posted.
			if form.is_valid():             #if the form is django's definiton for 'valid' then save it and redirect the user home.
				form.instance.user = request.user
				form.save()
				return redirect('step7_page')
		except:
			messages.success(request, 'Cannot resubmit. Please use "edit" instead.')
			return redirect('user-homepage')
	return render(request, 'form7.html', {'form':form} ) # return  this function to the form.html page and let it use form as s variable and call it's attributes (form.box1)


@login_required(login_url='login_user')  #sends user back to login page if they try to go to a view form in the address bar that isn't their's.
def Step7_Form_View(request):
	"""View for user to see completed form"""
	step7 = StepSeven.objects.filter(user=request.user) #user can only view there form. request user and filter the objects/forms for there step oneform.
	return render(request,'form_view7.html',{'step7': step7})

@login_required
def editpost7(request, step_seven ):
	"""Form1 Edit post function"""
	step_seven = StepSeven.objects.get(pk=step_seven)
	form7 = StepSevenForm(instance=step_seven)
	step7 = StepSeven.objects.filter(user=request.user)
	if request.method == 'POST':
		form7 = StepSevenForm(request.POST, instance=step_seven)
		if form6.is_valid():
			form6.save()
			return redirect('user-homepage')
	return render(request,'update_form7.html', {'form7': form7, 'step7': step7})

	

@login_required(login_url='login_user')
def Step7_Form_Delete(request, step_seven):
    form = StepSeven.objects.get(pk=step_seven)
    if request.method == "POST":
    	form.delete()
    	return redirect("user-homepage")
    context = {'form': form}
    return render(request, 'delete_form7.html', context)

        ###########Form8##############

@login_required(login_url='login_user')
def Step8_Form_Completion(request):
	"""Generates link for user to fill out form"""
	form = StepEightForm                #Assign the form to the variable in the function.
	if request.method == 'POST':     # if method or form is requested then POST or send data to this function. If someone is loggded in . . 
		try:
			form = StepEightForm(request.POST) #the method is form and it is to be posted.
			if form.is_valid():             #if the form is django's definiton for 'valid' then save it and redirect the user home.
				form.instance.user = request.user
				form.save()
				return redirect('step8_page')
		except:
			messages.success(request, 'Cannot resubmit. Please use "edit" instead.')
			return redirect('user-homepage')
	return render(request, 'form8.html', {'form':form} ) # return  this function to the form.html page and let it use form as s variable and call it's attributes (form.box1)


@login_required(login_url='login_user')  #sends user back to login page if they try to go to a view form in the address bar that isn't their's.
def Step8_Form_View(request):
	"""View for user to see completed form"""
	step8 = StepEight.objects.filter(user=request.user) #user can only view there form. request user and filter the objects/forms for there step oneform.
	return render(request,'form_view8.html',{'step8': step8})


@login_required
def editpost8(request, step_eight ):
	"""Form1 Edit post function"""
	step_eight = StepEight.objects.get(pk=step_eight)
	form8 = StepEightForm(instance=step_eight)
	step8 = StepEight.objects.filter(user=request.user) # seperate this from teh function so it still works when no form has been completed.
	if request.method == 'POST':
		form8 = StepEightForm(request.POST, instance=step_eight)
		if form8.is_valid():
			form8.save()
			return redirect('user-homepage')
	return render(request,'update_form8.html', {'form8': form8, 'step8': step8})

@login_required(login_url='login_user')
def Step8_Form_Delete(request, step_eight):
    form = StepEight.objects.get(pk=step_eight)
    if request.method == "POST":
    	form.delete()
    	return redirect("user-homepage")
    context = {'form': form}
    return render(request, 'delete_form8.html', context)

        ###########Form9##############

