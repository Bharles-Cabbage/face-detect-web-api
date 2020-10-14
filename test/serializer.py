from rest_framework import serializers

class ImageLinkSerializer(serializers.Serializer):
    image_url = serializers.CharField(required=False)

    # image = serializers.ImageField(read_only=True, required=False)

