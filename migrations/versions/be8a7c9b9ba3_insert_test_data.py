"""Insert test data

Revision ID: be8a7c9b9ba3
Revises: 143b57dec846
Create Date: 2024-04-22 21:39:28.362034

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'be8a7c9b9ba3'
down_revision: Union[str, None] = '143b57dec846'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("INSERT INTO identifier (telegram_id) VALUES (1234), (1200), (333), (4321);")


def downgrade() -> None:
    op.execute("TRUNCATE identifier")
