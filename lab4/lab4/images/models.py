from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    url = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} -> {self.title}"