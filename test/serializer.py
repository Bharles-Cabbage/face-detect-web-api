from rest_framework import serializers

class ImageLinkSerializer(serializers.Serializer):
    link = serializers.CharField()