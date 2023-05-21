from django.db import models
from django.core.validators import MaxValueValidator



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

