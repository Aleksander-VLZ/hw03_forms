from django.db import models
# Из модуля auth импортируем функцию get_user_model
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):  # наследник класса Model из модуля models
    title = models.CharField(
        max_length=200,
        verbose_name='Название сообщества'
    )
    slug = models.SlugField(
        unique=True,
        max_length=200,
        verbose_name='URL'
    )
    description = models.TextField(
        verbose_name='Описание сообщества'
    )

    def __str__(self) -> str:
        return self.title


class Post(models.Model):  # наследник класса Model из модуля models
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name='Группа'
    )

    def __str__(self) -> str:
        # выводим текст поста
        return self.text

    class Meta:
        ordering = ['-pub_date']
