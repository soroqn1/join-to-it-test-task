from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    title = models.CharField(_("title"), max_length=255)
    description = models.TextField(_("description"), blank=True)
    date = models.DateTimeField(_("date and time"), db_index=True)
    location = models.CharField(_("location"), max_length=255, db_index=True)
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organized_events",
        verbose_name=_("organizer"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ["-date"]
        indexes = [
            models.Index(fields=["date", "location"]),
        ]

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%Y-%m-%d %H:%M')})"
