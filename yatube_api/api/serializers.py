from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model


from posts.models import Comment, Post, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        """
        Запретить подписку на самого себя.
        """
        request_user = self.context['request'].user
        if request_user == value:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя.'
            )
        return value

    def create(self, validated_data):
        """
        При создании подписки повязать поле user на текущего пользователя.
        """
        user = self.context['request'].user
        following = validated_data['following']
        return Follow.objects.create(user=user, following=following)
