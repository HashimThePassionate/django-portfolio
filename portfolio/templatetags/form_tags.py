# form_tags.py
from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    """ Add a CSS class to form fields """
    return value.as_widget(attrs={'class': arg})
