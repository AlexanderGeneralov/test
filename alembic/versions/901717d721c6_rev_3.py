"""rev 3

Revision ID: 901717d721c6
Revises: b19097ac8313
Create Date: 2026-02-26 22:34:20.983560

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '901717d721c6'
down_revision: Union[str, Sequence[str], None] = 'b19097ac8313'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
