from django.test import TestCase

from menu.models import Menu, MENU_TYPE_URL


class MenuTestCase(TestCase):

    def test_success_create_menu(self):
        created_menu = Menu.objects.create(
            name="Menu",
            type=MENU_TYPE_URL,
            url="https://ertai.kz"
        )

        self.assertEquals(created_menu.name, "Menu")
        self.assertEquals(created_menu.url, "https://ertai.kz")
        self.assertEquals(created_menu.position, None)
        self.assertEquals(created_menu.type, MENU_TYPE_URL)
