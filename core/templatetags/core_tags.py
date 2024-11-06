from constance import config
from django import template

register = template.Library()


@register.simple_tag()
def get_config():
    values = {}
    _config_keys = config.__dir__()

    for key in _config_keys:
        if key.startswith('PHONE'):
            _phone = getattr(config, key)
            phone = ''.join(list(filter(lambda x: x.isdigit(), _phone)))
            values[key] = (_phone, phone)
        else:
            values[str(key)] = getattr(config, key)
    return values
