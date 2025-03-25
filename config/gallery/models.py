from django.db import models

class Picture(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to="images/", null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
