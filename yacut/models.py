from datetime import datetime

from . import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dist(self, only_long_link=False):
        if only_long_link:
            return dict(url=self.original)
        return dict(url=self.original, short_link=self.short)

    def from_dict(self, data):
        matches = {'url': 'original', 'custom_id': 'short'}
        for key in matches.keys():
            if key in data:
                setattr(self, matches[key], data[key])
