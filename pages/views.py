from django.shortcuts import render
from pages.forms import ContactForm
from .models import ContactMessage

def home_page_view(request):
    context={
        'nom' :'ZEBI',
        'age' : '25',
        'coulleur' : ['Noir' , 'rouge','Bleu' , 'Maron' ],
        'est_connecte' : True
        
    }
    return render(request, 'home.html',context)



def contact_page_view(request):
    success_msg=None
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success_msg="votre message es bien été soumis !"
            form=ContactForm()
    else:
        form=ContactForm()
        context={
            'form':form,
            'success_msg':success_msg
        }
    return render (request, 'contact.html', context)


def a_propos_page_view(request):
    return render(request , 'a_propos.html')

def message_liste_view(request):
    messages=ContactMessage.objects.all()
    context={
        'messages_list': messages
    }
    return render(request ,'message_list.html',context )