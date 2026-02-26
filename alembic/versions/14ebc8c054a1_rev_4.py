"""rev 4

Revision ID: 14ebc8c054a1
Revises: 901717d721c6
Create Date: 2026-02-26 22:35:10.084159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '14ebc8c054a1'
down_revision: Union[str, Sequence[str], None] = '901717d721c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
