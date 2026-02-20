from django.db import models

# Create your models here.
class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
    )

    recipient = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='notifications')
    actor = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='sent_notifications')
    verb = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey('posts.Comment', on_delete=models.CASCADE, null=True, blank=True)
    like = models.ForeignKey('posts.Like', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification from {self.actor.username} to {self.recipient.username} - {self.notification_type}'