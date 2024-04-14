from .db import db


class Table(db.Model):
    __tablename__ = 'table'
    id = db.Column(db.Integer(), primary_key=True)

    @staticmethod
    def get_by_id(pk):
        return Table.query.filter_by(id=pk)

    def __repr__(self):
        return f'<Id {self.id}>'
