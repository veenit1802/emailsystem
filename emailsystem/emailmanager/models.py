from django.db import models


class EmailModel(models.Model):
    sender_mail = models.CharField(max_length=100)
    subject = models.CharField(max_length=150)
    body = models.CharField(max_length=400)
