"""add fks for philosophy_responses and profiles

Revision ID: 5ac2d0028e95
Revises: aa637e6f922b
Create Date: 2025-12-24 01:07:12.802916

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ac2d0028e95'
down_revision: Union[str, Sequence[str], None] = 'aa637e6f922b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
