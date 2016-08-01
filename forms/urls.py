
from django.conf.urls import url

from forms_app.views import ContactWizard

from django.views.generic import ListView

urlpatterns = [
    url(r"^$", ContactWizard.as_view())
]
