from django.db import models

# Create your models here.
class contact(models.Model):
    Name = models.TextField(max_length=30,null=True)
    Email_id = models.TextField(max_length=50,null=True)
    subject = models.TextField(max_length=200, null=True)
    message = models.TextField(max_length=500,null=True)