from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

User = get_user_model()


class Follow(models.Model):
    """
    Модель подписки: user подписывается на following.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='подписчик'
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='автор'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='prevent_self_follow'
            ),
        ]
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return f"{self.user.username} подписан на {self.following.username}"


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название группы'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальный URL-идентификатор'
    )
    description = models.TextField(
        verbose_name='Описание группы'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
