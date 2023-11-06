from django.urls import path

from personal_feed.views import UserFeedView

urlpatterns = [
    path('user/<int:user_id>/', UserFeedView.as_view(), name='feed-list'),
]
