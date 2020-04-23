from django import template

register = template.Library()


@register.simple_tag
def icons(icon_type):
    """A tag to return the correct Bulma icon class given an input type"""
    icons = {
            'text':'user',
            'email':'envelope',
            'password':'lock',
            }

    return icons[icon_type]

@register.simple_tag
def input_class(input_type):
    """A tag to get the correct Bulma input class given an input type to be used in forms"""
    input_class ={
            'text':'text',
            'email':'text',
            'password':'text',
            'checkbox':'checkbox',
            }

    return input_class[input_type]

