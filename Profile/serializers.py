from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    owner = serializers.CharField()
    country = serializers.CharField()
    city = serializers.CharField()
    telephone = serializers.CharField()
    age = serializers.IntegerField()
    rate = serializers.FloatField()
