from django.db import models
from django.contrib.auth.models import User


class Entity(models.Model):
    _id = models.AutoField(name="id", primary_key=True)
    key = models.TextField()
    kind = models.TextField()
    value = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.TextField(blank=True)
    created = models.DateTimeField()

    def __str__(self):
        return f"{self.kind}: {self.key}"
