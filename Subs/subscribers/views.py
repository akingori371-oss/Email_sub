from django.shortcuts import render

from .models import Subscriber


def subscribe(request):
    message = None
    message_type = "info"

    if request.method == "POST":
        email = (request.POST.get("email") or "").strip()

        if not email:
            message = "Please enter a valid email address."
            message_type = "error"
        elif Subscriber.objects.filter(email__iexact=email).exists():
            message = f"{email} is already subscribed."
            message_type = "warning"
        else:
            Subscriber.objects.create(email=email)
            message = f"Thanks! {email} has been subscribed."
            message_type = "success"

    return render(request, "subscribe.html", {"message": message, "message_type": message_type})
