from django import template
from django_menu.models import Menu
register = template.Library()
@register.inclusion_tag('django_menu/menu_structure.html')
def show_menu(model):
    cache = Menu.menu_manager.all()
    return {'context': [cache.get(text=model)]}