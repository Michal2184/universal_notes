from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def contact(request):
    messageSent = False
    topic = ""
    if request.method != 'POST':
        form = EmailForm()
    else:
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Contact Us - UniNotes User"
            message = cd['message']
            sender = cd['sender']
            # sending to recipient
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [sender])
            messageSent = True
    context = {'form': form, 'messageSent': messageSent}
    return render(request, 'mailer/contact.html', context)