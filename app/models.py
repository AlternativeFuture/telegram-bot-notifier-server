from .db import db


class Identifier(db.Model):
    __tablename__ = 'identifier'
    id = db.Column(db.Integer(), primary_key=True)
    telegram_id = db.Column(db.BigInteger())

    def __repr__(self):
        return f'<Id {self.telegram_id}>'
