from django.test    import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_str_method(self):
        """
        The __str__ method should return "title : price"
        """
        item = Menu.objects.create(
            title="IceCream",
            price="80.00",
            inventory=100
        )
        self.assertEqual(str(item), "IceCream : 80.00")
