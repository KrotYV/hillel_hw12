from django.contrib import messages
from django.shortcuts import redirect, render

from task_celery.tasks import send_mail as celery_send_mail

from .forms import Reminder


def index(request):
    if request.method == "POST":
        form = Reminder(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            date = form.cleaned_data['time']
            celery_send_mail.apply_async([email, message], eta=date)
            messages.add_message(request, messages.SUCCESS, 'Message sent')
            return redirect('')
    else:
        form = Reminder()

    return render(request, "index.html", context={"form": form})
