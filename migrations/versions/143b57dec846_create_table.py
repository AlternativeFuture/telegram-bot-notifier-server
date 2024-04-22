"""Create table

Revision ID: 143b57dec846
Revises: 
Create Date: 2024-04-14 19:34:03.916403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '143b57dec846'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'identifier',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('telegram_id', sa.BigInteger),
    )


def downgrade() -> None:
    op.drop_table('identifier')
