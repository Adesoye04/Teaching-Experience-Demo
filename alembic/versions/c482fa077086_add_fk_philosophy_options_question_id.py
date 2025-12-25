"""add fk philosophy_options.question_id

Revision ID: c482fa077086
Revises: 75352e312941
Create Date: 2025-12-23 22:01:56.996605

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c482fa077086'
down_revision: Union[str, Sequence[str], None] = '75352e312941'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("philosophy_options") as batch_op:
        batch_op.alter_column("question_id", existing_type=sa.Integer(), nullable=False)
        batch_op.create_foreign_key(
        "fk_philosophy_options_question_id",
        "philosophy_questions",
        ["question_id"],
        ["id"],
            ondelete = "CASCADE",
        )

def downgrade() -> None:
    with op.batch_alter_table("philosophy_options") as batch_op:
        batch_op.drop_constraint("fk_philosophy_options_question_id", type_="foreignkey")
