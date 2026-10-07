from django.shortcuts import render
from .models import Subscriber

def subscribe(request):
  if request.method == "POST":
    email = request.POST.get("email")

    existing = Subscriber.objects.filter(email = email).exists()
    if existing :
     print(f"{email} already exists")   
    else:
       Subscriber.objects.create(email=email)

  return render(request, "subscribe.html")   
