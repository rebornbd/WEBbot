from django.db import models


class Appuser(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Phonenum(models.Model):
    number = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(Appuser, related_name='nums', on_delete=models.CASCADE)

    def __str__(self):
        return self.number

