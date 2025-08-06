from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)        # new field

    def __str__(self):
        return f"Photo {self.id} uploaded at {self.uploaded_at}"
