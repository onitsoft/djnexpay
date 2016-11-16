from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class MainPageTest(TestCase):

    def setUp(self):
        self.c = Client()

    def test_main_page_access_is_good(self):
        response = self.c.get(reverse('core.main'))
        self.assertEqual(response.status_code, 200)

    def test_inexistent_opage_throws_not_found(self):
        response = self.c.get('/prueba')
        self.assertEqual(response.status_code, 404)

    def test_calling_order_ajax_fails_with_nodata(self):
        response = self.c.get(reverse('core.ajax_order'))
        self.assertEqual(response.status_code, 404)
