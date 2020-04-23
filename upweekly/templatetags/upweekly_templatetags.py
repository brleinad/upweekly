from django import template

register = template.Library()


@register.simple_tag
def icons(icon_type):
    icons = {
            'text':'user',
            'email':'envelope',
            'password':'lock',
            }

    return icons[icon_type]
