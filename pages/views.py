from django.shortcuts import render
from django.http import HttpResponse
from pages.admin import ContactMessage

def home_page_view(request):
    context={
        'nom' :'ZEBI',
        'age' : '25',
        'coulleur' : ['Noir' , 'rouge','Bleu' , 'Maron' ],
        'est_connecte' : True
        
    }
    return render(request, 'home.html',context)



def contact_page_view(request):
    return render (request, 'contact.html')


def a_propos_page_view(request):
    return render(request , 'a_propos.html')

def message_liste_view(request):
    messages=ContactMessage.objects.all()
    context={
        'messages_list': messages
    }
    return render(request ,'message_list.html',context )