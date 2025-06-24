import json
from django import template

register = template.Library()

@register.filter(name='from_json')
def from_json(value):
    if isinstance(value, str):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return None
    return value 