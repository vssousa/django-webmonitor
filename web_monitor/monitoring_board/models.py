from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=200, unique=True)
    name = models.CharField(max_length=500)

    def __str__(self):
        return "Contact(" + str(self.id) + "," + self.name + "," + self.email + ")"


class Page(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return "Page(" + self.url + "," + str(self.date) + ")"
