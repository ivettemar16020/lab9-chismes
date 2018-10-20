from django.test import TestCase

from .models import Chisme


class ChismeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Chisme.objects.create(title='first chisme')
        Chisme.objects.create(content='content here')

    def test_title_content(self):
        chisme = Chisme.objects.get(id=1)
        expected_object_name = f'{chisme.title}'
        self.assertEquals(expected_object_name, 'first chisme')

    def test_content_content(self):
        chisme = Chisme.objects.get(id=2)
        expected_object_name = f'{chisme.content}'
        self.assertEquals(expected_object_name, 'content here')