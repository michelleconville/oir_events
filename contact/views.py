from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Thank you for your email"
            message = "Our team will contact you shortly."
            email_from = settings.EMAIL_HOST_USER
            email = form.cleaned_data["email"]
            recipient_list = email
            send_mail(subject, message, email_from, [recipient_list])
        return render(request, "contact/response.html")
    form = ContactForm()
    context = {"form": form}
    return render(request, "contact/contact.html", context)
