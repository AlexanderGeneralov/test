"""change User model name

Revision ID: 4177354fddd4
Revises: 89ada322c06d
Create Date: 2025-12-28 22:55:45.083588

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4177354fddd4'
down_revision: Union[str, Sequence[str], None] = '89ada322c06d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
