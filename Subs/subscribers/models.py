from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()

    def subscription_made():
     created_at = models.DateTimeField(auto_now_add=True)  
