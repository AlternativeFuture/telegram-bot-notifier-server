from .db import db


class Identifier(db.Model):
    __tablename__ = 'identifier'
    id = db.Column(db.Integer(), primary_key=True)
    telegram_id = db.Column(db.BigInteger())

    @staticmethod
    def get_by_id(telegram_id):
        return Identifier.query.filter_by(telegram_id=telegram_id).first()

    def __repr__(self):
        return f'<Id {self.telegram_id}>'
