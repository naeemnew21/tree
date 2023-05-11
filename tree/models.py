from django.db import models
from django.core.validators import MaxValueValidator



class Person(models.Model):
    name = models.CharField(max_length= 20, blank=False, null=False)
    fname  = models.CharField(max_length= 20, blank=False, null=False)
    birth = models.PositiveIntegerField(validators = [MaxValueValidator(1445)], null = True, blank = True)
    death = models.PositiveIntegerField(validators = [MaxValueValidator(1445)], null = True, blank = True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null = True, blank = True)
    rank   = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.parent:
            self.rank = self.parent.rank + 1 # determine rank of child
        super().save(*args, **kwargs)

