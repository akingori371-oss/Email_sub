from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def subscription_made(self):
        return f"Subscribed: {self.email}"

