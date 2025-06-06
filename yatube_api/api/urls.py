from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
]
