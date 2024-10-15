from django.db import models

# Create your models here.

class Job(models.Model):
    # Image - with folder to upload the image to
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=200)
    def __str__(self):
        return self.summary
