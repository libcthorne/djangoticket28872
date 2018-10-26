from django.contrib.postgres.fields import JSONField
from django.db import models


class MyModel1(models.Model):
    resource = JSONField()


class MyModel2(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=255,
    )
