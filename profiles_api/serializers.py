from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializers a name field for testing our api view"""
    name = serializers.CharField(max_length=10)
    last_name = serializers.CharField(max_length=10)
