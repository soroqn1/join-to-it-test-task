from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_registration_email(user_email, event_title, event_date, location):
    """Celery task to send email confirmation when a user registers for an event."""
    subject = f"Registration Confirmation: {event_title}"
    message = (
        f"Hello!\n\n"
        f"You have successfully registered for the event '{event_title}'.\n"
        f"Date: {event_date}\n"
        f"Location: {location}\n\n"
        f"Thank you for participating!"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, [user_email], fail_silently=False)
