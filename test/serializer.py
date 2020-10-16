from rest_framework import serializers

class ImageLinkSerializer(serializers.Serializer):
    image_url = serializers.CharField()

class ImageUploadSerializer(serializers.Serializer):
    image = serializers.ImageField()
    ext = serializers.CharField()

