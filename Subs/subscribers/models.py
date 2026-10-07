from django.db import models

class Members(models.Models):
    email = models.EmailField()

    def subscription_made():
     created_at = models.DateTimeField(auto_now_add=True)  
