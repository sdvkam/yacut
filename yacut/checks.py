import re

from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .utilities import get_unique_short_id


def validate_data(request):
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    validate_long_link(data)
    if data.get('custom_id') is None or data['custom_id'] == '':
        data['custom_id'] = get_unique_short_id(6)
        return data
    validate_short_link(data)
    return data


def validate_long_link(data):
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if (
        not isinstance(data['url'], str) or
        re.fullmatch(
            r'^https?:\/\/([\w\.]+)\.([a-z]{2,6}\.?)(\/[\w\.]*)*\/?$',
            data['url']
        ) is None
    ):
        raise InvalidAPIUsage(
            'Не корректная ссылка (должно быть, например: http://wow.com)'
        )


def validate_short_link(data):
    if (
        not isinstance(data['custom_id'], str) or
        len(data['custom_id']) > 16 or
        re.fullmatch(r'^[a-zA-Z0-9]+$', data['custom_id']) is None
    ):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URL_map.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')


def check_availability_short_link(link):
    url_map = URL_map.query.filter_by(short=link).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return url_map
