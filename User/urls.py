from django.urls import path
from .views import UserSearchView, FriendRequestView, FriendRequestActionView, FriendListView, PendingFriendRequestsView,ProfileView

urlpatterns = [
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-request/', FriendRequestView.as_view(), name='friend-request'),
    path('friend-request/<int:id>/', FriendRequestActionView.as_view(), name='friend-request-action'),
    path('friends/', FriendListView.as_view(), name='friend-list'),
    path('friend-requests/pending/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
    path('profile/', ProfileView.as_view(), name='profile'),
]