# -*- coding: utf-8 -*-
from datetime import datetime
from invitation import db


class Invitation(db.Model):
    __tablename__ = 'invitation'
    name = db.Column(db.String(64), primary_key=True)
    body = db.Column(db.UnicodeText)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name=None, body=None):
        self.name = name
        self.body = body

    def __unicode__(self):
        return self.name


def get_or_create(model, **kwargs):
    """SqlAlchemy implementation of Django's get_or_create.
    """
    session = db.session
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance
