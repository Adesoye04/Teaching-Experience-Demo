"""add tags to philosophy_options

Revision ID: d061b9934a15
Revises: 5ac2d0028e95
Create Date: 2025-12-24 01:56:09.509144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd061b9934a15'
down_revision: Union[str, Sequence[str], None] = '5ac2d0028e95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("philosophy_options") as batch_op:
        batch_op.add_column(sa.Column("primary_tag", sa.String(), nullable=True))
        batch_op.add_column(sa.Column("secondary_tag", sa.String(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("philosophy_options") as batch_op:
        batch_op.drop_column("secondary_tag")
        batch_op.drop_column("primary_tag")
