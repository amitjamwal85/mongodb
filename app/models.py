from django.db import models
import uuid


class Server(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    plan_id = models.CharField(max_length=15, null=False, default='P101')
    ram = models.CharField(max_length=10, null=True)
    hdd = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"{self.id}"


class ServerDetail(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    city = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f"{self.id}"
