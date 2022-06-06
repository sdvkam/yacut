from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app, db
from .checks import check_availability_short_link, validate_data
from .models import URL_map


@app.route('/api/id/', methods=['POST'])
def add_short_link():
    data = validate_data(request)
    url = URL_map()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    url.short = url_for(
        'redirect_short_link', short_link=url.short, _external=True)
    return jsonify(url.to_dist()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_link(short_id):
    url_map = check_availability_short_link(short_id)
    return jsonify(url_map.to_dist(only_long_link=True)), HTTPStatus.OK
