from .db import db


class Identifier(db.Model):
    __tablename__ = 'identifier'
    id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer())

    @staticmethod
    def get_by_id(pk):
        return Identifier.query.filter_by(product_id=pk).first()

    def __repr__(self):
        return f'<Id {self.product_id}>'
