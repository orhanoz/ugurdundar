from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"", include("home.urls") ),
    url(r"^blog/", include("pinax.blog.urls", namespace="pinax_blog")),
    url(r"^contact/", include("forms_app.urls", namespace="forms")),
    url(r"^iletisim/", include("home.urls", namespace="iletisim")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
