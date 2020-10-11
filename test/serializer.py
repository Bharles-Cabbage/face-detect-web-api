from rest_framework import serializers

class ImageLinkSerializer(serializers.Serializer):
    data = serializers.CharField()