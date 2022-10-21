from django.test import Client, TestCase
from django.urls import reverse

from ..models import Post, Group, User

LAST_POSTS: int = 10


class PaginatorViewsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username="Test_User",)
        cls.group = Group.objects.create(
            title="тест-группа",
            slug="test_group",
            description="тестирование",
        )
        for i in range(13):
            cls.post = Post.objects.create(
                text=f'Тестовый пост {i}',
                author=cls.user,
                group=Group.objects.get(slug='test_group'),
            )

    def setUp(self):
        #  Создаем неавторизованный клиент
        self.guest_client = Client()
        self.user = User.objects.get(username="Test_User")
        #  Создаем авторизованый клиент
        self.authorized_client = Client()
        #  Авторизуем пользователя
        self.authorized_client.force_login(self.user)

    def test_paginator_correct_context(self):
        templates = [
            reverse('posts:index'),
            reverse('posts:profile', kwargs={'username': 'Test_User'}),
            reverse('posts:group_list', kwargs={'slug': 'test_group'}),
        ]
        for template in templates:
            with self.subTest(template=template):
                response = self.guest_client.get(template)
                self.assertEqual(len(response.context['page_obj']), LAST_POSTS)

    def second_test_paginator_correct_context(self):
        templates = [
            reverse('posts:index'),
            reverse('posts:profile', kwargs={'username': 'Test_User'}),
            reverse('posts:group_list', kwargs={'slug': 'test_group'}),
        ]
        for template in templates:
            with self.subTest(template=template):
                response = self.guest_client.get(template + '?page=2')
                self.assertEqual(len(response.context['page_obj']), 3)
