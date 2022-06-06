from random import choices

from settings import set_symbols

from .models import URL_map


def get_unique_short_id(num):
    while True:
        short_link = ''.join(choices(set_symbols, k=num))
        if not URL_map.query.filter_by(short=short_link).first():
            break
    return short_link