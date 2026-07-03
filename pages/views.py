from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request):
    context={
        'nom' :'ZEBI',
        'age' : '25',
        'coulleur' : ['Noir' , 'rouge' ],
        'est_connecte' : True
    }
    return render(request, 'home.html',context)



def contact_page_view(request):
    return render (request, 'contact.html')


def a_propos_page_view(request):
    return render(request , 'a_propos.html')