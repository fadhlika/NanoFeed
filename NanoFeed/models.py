from flask_sqlalchemy import SQLAlchemy
from time import mktime
from datetime import datetime
db = SQLAlchemy()

class Channel(db.Model):
    """Model for channel data object"""
    __tablename__ = 'channel'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode(80))
    link = db.Column(db.Unicode(100))
        
    def __init__(self, name, link):
        self.name = name
        self.link = link

class Item(db.Model):
    """Model for item data object"""
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Unicode(80))
    date = db.Column(db.DateTime)
    link = db.Column(db.Unicode(100))
    thumbnail = db.Column(db.Unicode(100))
    summary = db.Column(db.Text)
    description = db.Column(db.Text)

    channel_id = db.Column(db.Integer, db.ForeignKey('channel.id'))
    channel = db.relationship('Channel', backref=db.backref('channel', lazy='dynamic'))
    def __init__(self, title, date, link, thumbnail, summary, description, channel):
        self.title = title
        self.date = datetime.fromtimestamp(mktime(date))
        self.link = link
        self.thumbnail = thumbnail
        self.summary = summary
        self.description = description
        self.channel = channel
    