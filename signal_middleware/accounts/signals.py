from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, **kwargs):
    """notify to user through email"""

    if kwargs.get("created", False):
        subject = "Welcome to Signal Middleware Project"
        message = f"Hello {instance.email}, thank you for registering!"
        from_email = "admin@example.com"
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)
