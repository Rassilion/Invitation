# -*- coding: utf-8 -*-
from invitation import db, Invitation

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    inv = Invitation('janeandjohn', 'Jane & John', 'You all know us. And we all know you. We are getting married.')
    db.session.add(inv)
    db.session.commit()
