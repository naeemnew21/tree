from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError





def validate_name(name):
    if not(name) or name.isspace():
        raise ValidationError('empty name is not valid name')  




class MyUser(AbstractUser):
    email         = models.EmailField(unique=True, blank=False, null=False)
    phone_regex   = RegexValidator(regex="[0][1][0125][0-9][ ]?\d{3}[ ]?\d{4}", message="Phone number must be entered in the format: '01xx xxx xxxx'. Up to 11 digits allowed.")
    phone         = models.CharField(validators=[phone_regex], max_length=11, blank=False, null=False) # validators should be a list
    first_name    = models.CharField(validators=[validate_name], max_length=30, blank=False, null=False)
    last_name     = models.CharField(validators=[validate_name], max_length=30, blank=False, null=False)
    
    REQUIRED_FIELDS = ['email', 'first_name']
    

    def __str__(self):
        return self.email

    
    @property
    def get_name(self):
        name = self.first_name
        if self.last_name:
            name += ' ' + self.last_name
        return name
        
    