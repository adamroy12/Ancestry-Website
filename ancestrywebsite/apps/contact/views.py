from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail

from ancestrywebsite import settings

from .forms import ContactForm


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            email = form.cleaned_data["email"]
            phonenumber = form.cleaned_data["phonenumber"]
            send_mail(f"{name} sent an email. {phonenumber}", message, email, [settings.DEFAULT_FROM_EMAIL])
            return render(request, 'contact.html', {"form": form, "success": True})
    else:
        raise NotImplementedError
    
    return render(request, 'contact.html', {"form": form})
