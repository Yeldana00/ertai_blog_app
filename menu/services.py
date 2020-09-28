from menu.models import Menu


def get_nav_menu():
    return Menu.objects.all().order_by('position')
