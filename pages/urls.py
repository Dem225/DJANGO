from django.urls import path
from .import views

urlpatterns=[
path('',views.home_page_view),
path("contact/",views.contact_page_view),
path("a_propos/", views.a_propos_page_view),
path("message_list/",views.message_liste_view)
]