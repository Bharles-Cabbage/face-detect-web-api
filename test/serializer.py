from rest_framework import serializers

class ImageLinkSerializer(serializers.Serializer):
    image_url = serializers.CharField()


