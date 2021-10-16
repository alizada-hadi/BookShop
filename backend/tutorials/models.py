from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=200, blank=True, default="")
    description = models.TextField()
    published = models.BooleanField(default=False)


    def __str__(self):
        return self.title
        