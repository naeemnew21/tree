from django.db import models
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length= 50, blank=False, null=False)
    fname  = models.TextField(null = True, blank = True)
    url   = models.URLField(default="", null = True, blank = True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True)
    rank   = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.get_fname

    def save(self, *args, **kwargs):
        if self.parent:
            self.rank = self.parent.rank + 1 # determine rank of child
        super().save(*args, **kwargs)

    @property
    def get_fname(self):
        name = self.name
        if self.parent:
            name += '-' + self.parent.get_fname
        return name



class Family(models.Model):
    name = models.CharField(max_length= 20, blank=False, null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True)
    rank   = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.get_fname

    def save(self, *args, **kwargs):
        if self.parent:
            self.rank = self.parent.rank + 1 # determine rank of child
        super().save(*args, **kwargs)

    @property
    def get_fname(self):
        name = self.name
        if self.parent:
            name += ' ' + self.parent.get_fname
        return name



def summer_time():
    return timezone.now() + timezone.timedelta(hours=1)

class Hist(models.Model):
    date = models.DateTimeField(default=summer_time)

class Log_Info(models.Model):
    ip               = models.CharField(max_length= 200, blank=True, null=True)
    device_type      = models.CharField(max_length= 200, blank=True, null=True)
    browser_type     = models.CharField(max_length= 200, blank=True, null=True)
    browser_version  = models.CharField(max_length= 200, blank=True, null=True)
    os_type          = models.CharField(max_length= 200, blank=True, null=True)
    os_version       = models.CharField(max_length= 200, blank=True, null=True)
    location_country = models.CharField(max_length= 200, blank=True, null=True)
    location_city    = models.CharField(max_length= 200, blank=True, null=True)
    history          = models.ManyToManyField(Hist, blank = True)

    def __str__(self):
        return self.ip