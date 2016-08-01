from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView
from forms_app.forms import ContactForm1 , ContactForm2, PersonalInformation , EducationInformation
from django.core.mail import send_mail

class ContactWizard(SessionWizardView):
	form_list = [PersonalInformation, EducationInformation]
	template_name= "forms/contact_form.html"
	def done(self , form_list , **kwargs):
		form_data = process_form_data(form_list)
		return render_to_response("forms/done.html", {"form_data" : form_data} )

def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]

	send_mail(form_data[0]["subject"],
	form_data[1]["message"],
	form_data[0]["sender"],
	["nebu.gomm@gmail.com"])

	return form_data
