from .db import db


class Identifier(db.Model):
    """
    Model representing identifiers stored in the database.

    Attributes:
        id (int): The unique identifier for the Identifier object (primary key).
        telegram_id (int): The Telegram ID associated with the Identifier.

    Methods:
        __repr__(): Returns a string representation of the Identifier object.

    Note:
        This model maps to the 'identifier' table in the database.
    """

    __tablename__ = 'identifier'
    id = db.Column(db.Integer(), primary_key=True)
    telegram_id = db.Column(db.BigInteger())

    def __repr__(self):
        return f'<Id {self.telegram_id}>'
