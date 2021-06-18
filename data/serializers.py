from rest_framework import serializers

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    father = serializers.CharField(max_length=50)
    age = serializers.IntegerField()