from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(
        User,
        related_name='notifications',
        on_delete=models.CASCADE
    )

    actor = models.ForeignKey(
        User,
        related_name='actions',
        on_delete=models.CASCADE
    )

    verb = models.CharField(max_length=255)

    # Generic relation fields
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE, null=True,
    blank=True
    )

    target = GenericForeignKey('content_type', 'object_id')
    object_id = models.PositiveIntegerField(null=True,
    blank=True)

    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target}"