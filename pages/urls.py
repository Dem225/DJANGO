from django.urls import path
from .import views

urlpatterns=[
# path('',views.home_page_view),
path('',views.HomepageView.as_view(),name='home'),
path('sigunp/',views.SignUpView.as_view(),name='sigunp'),
path("contact/",views.contact_page_view,name='contact'),
path("a_propos/", views.a_propos_page_view ,name='a_propos'),
path("message_list/",views.MessageListeViews.as_view(),name='message_list')


]