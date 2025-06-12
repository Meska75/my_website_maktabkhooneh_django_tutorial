from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect
from website.forms import ContactForm , NewsletterForm
from django.contrib import messages

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            edied_form = form.save(commit=False)
            edied_form.name = 'unknown'
            edied_form.save()
            messages.add_message(request, messages.SUCCESS, "Your message Successfully sended.")
        else:
            messages.add_message(request, messages.ERROR, "Problem in sending message.")
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method=='POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your Signin is Successfully.")
        else:
            messages.add_message(request, messages.ERROR, "Problemin  Signin.")
            
        referer = request.META.get('HTTP_REFERER', '/')
        return redirect(referer)

