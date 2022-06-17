
from dataclasses import field
from rest_framework import serializers
from .models import Puppies



class PuppiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Puppies
        fields="__all__"
        # fields=["name","age"]