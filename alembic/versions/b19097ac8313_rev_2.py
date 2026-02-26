"""rev 2

Revision ID: b19097ac8313
Revises: 08cc43ac26b5
Create Date: 2026-02-26 22:24:37.163881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b19097ac8313'
down_revision: Union[str, Sequence[str], None] = '08cc43ac26b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
