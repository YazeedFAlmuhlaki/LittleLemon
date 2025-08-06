from django.test           import TestCase
from django.urls          import reverse
from rest_framework        import status
from rest_framework.test   import APIClient

from restaurant.models      import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # create a few items
        Menu.objects.create(title="IceCream", price="80.00", inventory=100)
        Menu.objects.create(title="Burger"  , price="150.00", inventory= 50)
        # assume you registered your viewset under the basename "menu"
        self.url = reverse('menu-list')

    def test_get_all_menu_items(self):
        """
        GET /<api_prefix>/menu/ should return all menu items serialized.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        qs         = Menu.objects.all()
        serializer = MenuSerializer(qs, many=True)
        self.assertEqual(response.data, serializer.data)
