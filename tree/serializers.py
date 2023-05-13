
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from .models import Person




class BranchUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name',
                  'fname', 
                  'url',
                   ]
        


class BranchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'