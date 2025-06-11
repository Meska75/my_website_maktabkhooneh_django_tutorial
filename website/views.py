from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from website.forms import ContactForm , NewsletterForm

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('not valid')

    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method=='POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks!")
        else:
            HttpResponseRedirect('/')

