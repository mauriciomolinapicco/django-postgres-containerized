from django.db import models

# Create your models here.

class Connection(models.Model):
    name = models.CharField(max_length=200)
    is_connected = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Connection {self.name} is active: {self.is_connected}"