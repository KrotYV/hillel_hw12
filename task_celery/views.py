from django.contrib import messages
from django.shortcuts import redirect, render

from task_celery.tasks import send_mail as celery_send_mail

from .forms import Reminder


def index(request):
    if request.method == "GET":
        form = Reminder()
    else:
        form = Reminder(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # date = form.cleaned_data['time']
            celery_send_mail.delay(email, message)
            messages.add_message(request, messages.SUCCESS, 'Message sent')
            return redirect("task_celery")
    return render(request, "index.html", context={"form": form})
