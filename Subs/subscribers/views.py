from django.shortcuts import render
from django.core.mail import send_mail
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

            # Normal message
            email_message = (
                "Thank you for subscribing to our newsletter!"
            )

            # Special message for Anthony
            if email.lower() == "anthonydev371@gmail.com":
                email_message = (
                    "This text is sent to you by Anthony for confirming a feature, "
                    "if it worked just alert him so that he can finally get some sleep!"
                )

            send_mail(
                "This is Anthony testing out a backend feature "
                "(im jus trying to be professional here i actually dont care "
                "jus bare with it)",
                email_message,
                None,
                [email],
            )

            message = "You have successfully subscribed!"
            message_type = "success"

    return render(
        request,
        "subscribe.html",
        {
            "message": message,
            "message_type": message_type
        }
    )