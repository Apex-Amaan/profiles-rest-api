from rest_framework import serializers


class HelloSerializers(serializers.Serializer):

    name=serializers.CharField(max_length=10)

    age = serializers.IntegerField(default=18)
