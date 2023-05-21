
from rest_framework import serializers
from .models import Person, Family




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



class FamilyBranchUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['name',
                   ]



class FamilyBranchCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'