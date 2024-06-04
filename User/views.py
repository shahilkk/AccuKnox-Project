from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import *
from .serializers import UserSerializer, FriendRequestSerializer ,ProfileSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import status, permissions
from geopy.geocoders import Nominatim




class UserPagination(PageNumberPagination):
    page_size = 10


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = UserPagination

    def get_queryset(self):
        search_term = self.request.query_params.get('search', '')
        if search_term:
            return User.objects.filter(Q(email__iexact=search_term) | Q(first_name__icontains=search_term) | Q(last_name__icontains=search_term) | Q(username__icontains=search_term))
        return User.objects.none()

class FriendRequestView(generics.CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        to_user = User.objects.get(id=self.request.data['to_user'])
        serializer.save(from_user=self.request.user, to_user=to_user)

class FriendRequestActionView(generics.UpdateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [AllowAny]
    queryset = FriendRequest.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.to_user != request.user:
            return Response({"detail": "Not allowed."}, status=status.HTTP_403_FORBIDDEN)
        status_ = request.data.get('status')
        if status_ in ['accepted', 'rejected']:
            instance.status = status_
            instance.save()
            return Response(self.get_serializer(instance).data)
        return Response({"detail": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)

class FriendListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.filter(sent_requests__to_user=self.request.user, sent_requests__status='accepted') | \
               User.objects.filter(received_requests__from_user=self.request.user, received_requests__status='accepted')

class PendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')




class ProfileView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        profile = request.user.profile
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # Check if profile exists, create one if it doesn't
        profile, created = Profile.objects.get_or_create(user=user)

        # Update profile fields
        profile.bio = data.get('bio', profile.bio)
        profile.location = data.get('location', profile.location)
        if 'profile_picture' in data:
            profile.profile_picture = data['profile_picture']

        # Geocode the location if provided
        if profile.location:
            geolocator = Nominatim(user_agent="AccuKnox_User")
            print('\n\n\n',geolocator,'\n\n')
            location = geolocator.geocode(profile.location)
            print('\n\n\n',location,'\n\n')
            if location:
                profile.latitude = location.latitude
                profile.longitude = location.longitude

        profile.save()

        serializer = self.serializer_class(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)