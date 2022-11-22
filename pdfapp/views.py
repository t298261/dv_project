from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from myapp.views import *


### PDF VIEWS ###

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def generate_pdf(request, *args, **kwargs):
	template = get_template('pdfapp/step_one_pdf.html')
	form1 = StepOne.objects.filter(user=request.user)
	step1 = StepOne.objects.filter(user=request.user)
	data = { 
		'form1': form1,
		'step1': step1
	}
	html = template.render(data)
	pdf = render_to_pdf('pdfapp/step_one_pdf.html', data )
	if pdf:
		return HttpResponse(pdf, content_type="application/pdf")
	else:
		return HttpResponse("PDF Not Found.")

def generate_pdf2(request, *args, **kwargs):
	template = get_template('pdfapp/step_two_pdf.html')
	form = StepTwo.objects.filter(user=request.user)
	step = StepTwo.objects.filter(user=request.user)
	data = { 
		'form': form,
		'step': step
	}
	html = template.render(data)
	pdf = render_to_pdf('pdfapp/step_two_pdf.html', data )
	if pdf:
		return HttpResponse(pdf, content_type="application/pdf")
	else:
		return HttpResponse("PDF Not Found.")

def generate_pdf3(request, *args, **kwargs):
	template = get_template('pdfapp/step_three_pdf.html')
	form = StepThree.objects.filter(user=request.user)
	step = StepThree.objects.filter(user=request.user)
	data = { 
		'form': form,
		'step': step
	}
	html = template.render(data)
	pdf = render_to_pdf('pdfapp/step_three_pdf.html', data )
	if pdf:
		return HttpResponse(pdf, content_type="application/pdf")
	else:
		return HttpResponse("PDF Not Found.")

def generate_pdf4(request, *args, **kwargs):
	template = get_template('pdfapp/step_four_pdf.html')
	form = StepFour.objects.filter(user=request.user)
	step = StepFour.objects.filter(user=request.user)
	data = { 
		'form': form,
		'step': step
	}
	html = template.render(data)
	pdf = render_to_pdf('pdfapp/step_Four_pdf.html', data )
	if pdf:
		return HttpResponse(pdf, content_type="application/pdf")
	else:
		return HttpResponse("PDF Not Found.")


#### FORCED DOWNLOADS ###


def auto_download_pdf1(request, *args, **kwargs):
	template = get_template('pdfapp/step_one_pdf.html')
	form1 = StepOne.objects.filter(user=request.user)
	step1 = StepOne.objects.filter(user=request.user)
	data = { 
		'form1': form1,
		'step1': step1
	}
	html = template.render(data)
	pdf = render_to_pdf('pdfapp/step_one_pdf.html', data )
	if pdf:
		pdf['Content-Disposition'] = 'attachment; filename="Safety during a violent incident.pdf"'
		return pdf
	else:
		return HttpResponse("PDF Not Found.")

def auto_download_pdf2(request, *args, **kwargs):
	template = get_template('pdfapp/step_two_pdf.html')
	form = StepTwo.objects.filter(user=request.user)
	step = StepTwo.objects.filter(user=request.user)
	data = { 
		'form': form,
		'step': step
	}
	html = template.render(data)
	pdf = render_to_pdf('pdfapp/step_two_pdf.html', data )
	if pdf:
		pdf['Content-Disposition'] = 'attachment; filename="Safety when preparing to leave."'
		return pdf
	else:
		return HttpResponse("PDF Not Found.")

def auto_download_pdf3(request, *args, **kwargs):
	template = get_template('pdfapp/step_three_pdf.html')
	form = StepTwo.objects.filter(user=request.user)
	step = StepTwo.objects.filter(user=request.user)
	data = { 
		'form': form,
		'step': step
	}
	html = template.render(data)
	pdf = render_to_pdf('pdfapp/step_three_pdf.html', data )
	if pdf:
		pdf['Content-Disposition'] = 'attachment; filename="Safety in my own residence."'
		return pdf
	else:
		return HttpResponse("PDF Not Found.")

def auto_download_pdf4(request, *args, **kwargs):
	template = get_template('pdfapp/step_four_pdf.html')
	form = StepFour.objects.filter(user=request.user)
	step = StepFour.objects.filter(user=request.user)
	data = { 
		'form': form,
		'step': step
	}
	html = template.render(data)
	pdf = render_to_pdf('pdfapp/step_four_pdf.html', data )
	if pdf:
		pdf['Content-Disposition'] = 'attachment; filename="Safety: Protective & Restraining Orders"'
		return pdf
	else:
		return HttpResponse("PDF Not Found.")
	

