from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app1.models import App


class ViewTestCase(TestCase):

    def test_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        user = User.objects.get(username='user')
        self.assertEqual(App.objects.filter(create_by=user).count(), 2)
