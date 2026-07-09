from django import forms
from .models import ContactMessage
from .models import inscription_page
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields=["name","email" ,"message"]





class InscriptionForm(forms.ModelForm):
    class Meta:
        model =inscription_page
        fields=["name","role","matricule","user_name","pass_word"]
    