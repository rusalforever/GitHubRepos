from django.db import models


class Repo(models.Model):
    name = models.CharField(max_length=100)
    html_url = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    private = models.BooleanField()
    created_at = models.DateTimeField()
    watchers = models.IntegerField()
    body = models.TextField()

    class Meta:
        unique_together = ("name", "html_url")
