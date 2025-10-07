from django.db import models


class NewsletterSubscriber(models.Model):
    """Model to store newsletter subscriptions"""
    email = models.EmailField(unique=True)
    signup_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-signup_date']
    
    def __str__(self):
        return self.email