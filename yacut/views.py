from flask import flash, redirect, render_template

from . import app, db
from .forms import URL_mapForm
from .models import URL_map
from .utilities import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        short_link = form.custom_id.data
        if short_link:
            if URL_map.query.filter_by(short=short_link).first():
                flash(f'Имя {short_link} уже занято!')
                return render_template('main.html', form=form)
        else:
            short_link = get_unique_short_id(6)
        new_link = URL_map(
            original=form.original_link.data,
            short=short_link
        )
        form.custom_id.data = short_link
        db.session.add(new_link)
        db.session.commit()
        flash('Ваша новая ссылка готова')
    return render_template('main.html', form=form)


@app.route('/<short_link>')
def redirect_short_link(short_link):
    link_map = URL_map.query.filter_by(short=short_link).first_or_404()
    return redirect(link_map.original)
