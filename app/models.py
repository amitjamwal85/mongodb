from django.db import models


class Server(models.Model):
    plan_id = models.CharField(max_length=15, null=False, default='P101')
    ram = models.CharField(max_length=10, null=True)
    hdd = models.CharField(max_length=15, null=True)
