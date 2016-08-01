
from django.conf.urls import url


from django.views.generic import ListView
from pinax.blog.models import Post
from .views import ContactIzmirIndexView , ContactManisaIndexView , HomeIndexView

urlpatterns = [
    url(r"^$",HomeIndexView.as_view() , name="ana_sayfa"),
    url(r"^iletisim/izmir$", ContactIzmirIndexView.as_view() , name="izmir"),
    url(r"^iletisim/manisa$", ContactManisaIndexView.as_view() , name="manisa"),
]
