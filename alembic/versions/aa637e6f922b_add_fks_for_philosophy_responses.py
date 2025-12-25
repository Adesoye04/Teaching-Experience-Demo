"""add fks for philosophy_responses

Revision ID: aa637e6f922b
Revises: c482fa077086
Create Date: 2025-12-24 00:51:11.462069

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa637e6f922b'
down_revision: Union[str, Sequence[str], None] = 'c482fa077086'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("philosophy_responses") as batch_op:
        batch_op.alter_column("question_id", existing_type=sa.Integer(), nullable=False)
        batch_op.alter_column("option_id", existing_type=sa.Integer(), nullable=False)
        batch_op.alter_column("teacher_id", existing_type=sa.Integer(), nullable=False)
        batch_op.create_foreign_key(
            "fk_philosophy_responses_question_id",
        "philosophy_questions",
        ["question_id"],
            ["id"],
            ondelete = "CASCADE",
        )
        batch_op.create_foreign_key(
            "fk_philosophy_responses_option_id",
            "philosophy_options",
            ["option_id"],
            ["id"],
            ondelete="CASCADE",
        )
        batch_op.create_foreign_key(
            "fk_philosophy_responses_teacher_id",
            "teachers",
            ["teacher_id"],
            ["id"],
            ondelete = "CASCADE",
        )
    with op.batch_alter_table("philosophy_profiles") as batch_op:
        batch_op.alter_column("teacher_id", existing_type=sa.Integer(), nullable=False)
        batch_op.create_foreign_key(
            "fk_philosophy_profiles_teacher_id",
            "teachers",
            ["teacher_id"],
            ["id"],
            ondelete = "CASCADE",
        )


def downgrade() -> None:
    with op.batch_alter_table("philosophy_profiles") as batch_op:
        batch_op.drop_constraint("fk_philosophy_profiles_teacher_id", type_="foreignkey")
    with op.batch_alter_table("philosophy_responses") as batch_op:
        batch_op.drop_constraint("fk_philosophy_responses_question_id", type_="foreignkey")
        batch_op.drop_constraint("fk_philosophy_responses_option_id", type_="foreignkey")
        batch_op.drop_constraint("fk_philosophy_responses_teacher_id", type_="foreignkey")