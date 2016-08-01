from django.shortcuts import render
from formtools.wizard.views import SessionWizardView
from forms_app.forms import ContactForm1 ,PersonalInformation,EducationInformation


class JobApplicationWizard(SessionWizardView):
	form_list = [PersonalInformation , EducationInformation]
	template_name= "forms/application_form.html"
	def done(self , form_list , **kwargs):
		form_data = process_form_data(form_list)
		return render_to_response("forms/done.html", {"form_data" : form_data} )

class ContactWizard(SessionWizardView):
	form_list =[ContactForm1]
	template_name="forms/application_form.html"
def done(self , form_list , **kwargs):
	form_data = process_form_data(form_list)
	return render_to_response("forms/done.html", {"form_data" : form_data} )


def process_form_data(form_list):
	form_data = [form.cleaned_data for form in form_list]

	send_mail(form_data[0]["subject"],
	form_data[2]["message"], form_data[1]["sender"],
	["nebu.gomm@gmail.com"],fail_slient = False)
