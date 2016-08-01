
from django.conf.urls import url

from forms_app.views import JobApplicationWizard , ContactWizard

from django.views.generic import ListView

urlpatterns = [
    url(r"^is-basvurusu$", JobApplicationWizard.as_view(),name="is-basvurusu"),
    url(r"^mail-gönder$", ContactWizard.as_view(),name="mail-gönder")
]
