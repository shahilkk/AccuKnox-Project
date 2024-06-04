
from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']


class LikeSerializer(serializers.RelatedField):
    def to_representation(self, value):
        User = get_user_model()
        user = User.objects.get(id=value.id)
        return user.username


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    like_count = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'like_count', 'comments', 'likes']