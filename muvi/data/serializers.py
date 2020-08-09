from rest_framework import serializers
from data.models import content,User_data

class contentSerializer(serializers.ModelSerializer):
    class Meta:
        model=content
        fields=("__all__")


class User_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_data
        fields=("__all__")