from rest_framework import serializers
from .models import *

class EmpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = account1
        fields= '__all__'