from db import db


class Table(db.Model):
    __tablename__ = 'table'
    id = db.Column(db.Integer(), primary_key=True)

    def get_by_id(self, pk):
        self.query.filter_by(id=pk).all()

    def __repr__(self):
        return f'<Id {self.id}>'
