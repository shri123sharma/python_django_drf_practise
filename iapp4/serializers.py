from rest_framework import serializers


class CommentSeralizer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=100)
    created = serializers.DateTimeField()
