import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4,editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name
    
class Cafe(models.Model):
    cafe_uuid = models.UUIDField(default=uuid.uuid4,editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name
    
class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4,editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    def __str__(self) -> str:
        return self.customer_name