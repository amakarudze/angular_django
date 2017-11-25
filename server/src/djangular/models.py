from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=100)
    embed = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    featured = models.BooleanField(default=False)

    class Meta:
        managed = True

    def __str__(self):
        return self.name

