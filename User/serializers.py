from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from .models import User, FriendRequest,Profile
from django.utils import timezone
from datetime import timedelta


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'status', 'created_at']
        read_only_fields = ['from_user', 'created_at','status']

    def validate(self, data):
        from_user = self.context['request'].user
        now = timezone.now()
        one_minute_ago = now - timedelta(minutes=1)
        
        recent_requests_count = FriendRequest.objects.filter(
            from_user=from_user,
            created_at__gte=one_minute_ago
        ).count()

        if recent_requests_count >= 3:
            raise serializers.ValidationError("You can send a maximum of 3 friend requests per minute.")
        
        return data

    def create(self, validated_data):
        validated_data['from_user'] = self.context['request'].user
        return super().create(validated_data)



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'latitude', 'longitude', 'profile_picture']
        read_only_fields = ['latitude', 'longitude']