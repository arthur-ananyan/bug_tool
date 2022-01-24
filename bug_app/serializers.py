from rest_framework import serializers
from .models import Bug, Comment


class BugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = '__all__'

    def create(self, validated_data):
        return Bug.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)