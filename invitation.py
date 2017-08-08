from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

#  Logging
import logging

logging.basicConfig(
    level=app.config['LOG_LEVEL'],
    format='%(asctime)s %(levelname)s: %(message)s '
           '[in %(pathname)s:%(lineno)d]',
    datefmt='%Y%m%d-%H:%M%p',

)


# model
class Invitation(db.Model):
    __tablename__ = 'invitation'
    url = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64))
    body = db.Column(db.UnicodeText)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, url=None, name=None, body=None):
        self.url = url
        self.name = name
        self.body = body

    def __unicode__(self):
        return self.name


# views
@app.route("/", subdomain="<name>")
@app.route('/inv/<name>')
def invitation_render(name):
    inv = Invitation.query.filter_by(url=name).first()
    if inv:
        return render_template('1/index.html', inv=inv)
    else:
        return '404'


if __name__ == '__main__':
    app.run()
