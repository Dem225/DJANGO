
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("pages.urls")),
    path("/a_propos", include("pages.urls")),
    path("contact/",include("pages.urls")),
    path("/message_list", include("pages.urls")),
    path('compte/', include("django.contrib.auth.urls",))
]
