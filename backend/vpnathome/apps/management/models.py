from django.db import models


class Settings(models.Model):

    email_enabled = models.BooleanField(default=False)
    registration_enabled = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'settings'
        verbose_name_plural = 'settings'

    def __str__(self):
        return 'Settings pk={id}'.format(id=self.id)

    @staticmethod
    def instance():
        return Settings.objects.first()


class BlockListUrl(models.Model):
    url = models.URLField(unique=True)
    enabled = models.BooleanField(default=False)
    count = models.IntegerField(null=True, default=None)


class BlockedDomain(models.Model):
    domain = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.id} - {self.domain}"

