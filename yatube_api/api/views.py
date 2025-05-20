from rest_framework import viewsets, mixins, permissions, filters
from posts.models import Follow
from .serializers import FollowSerializer


class FollowViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """
    Эндпоинт /follow/:
    GET   — список подписок текущего пользователя
    (search по following__username)
    POST  — подписаться на пользователя
    """
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
