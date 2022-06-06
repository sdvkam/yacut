from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Regexp(
                r'^https?:\/\/([\w\.]+)\.([a-z]{2,6}\.?)(\/[\w\.]*)*\/?$',
                message='Введите корректную ссылку (пример: http://wow.com)'
            ),
            Length(1, 256)
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Regexp(
                r'^[a-zA-Z0-9]+$',
                message='Используйте только буквы латинского алфавита и цифры'
            ),
            Optional(strip_whitespace=False)
        ]
    )
    submit = SubmitField('Добавить')
