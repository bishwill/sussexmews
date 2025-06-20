"""todo table

Revision ID: 85c6990a99e8
Revises: d267bceacfbc
Create Date: 2025-06-20 09:44:01.625478

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "85c6990a99e8"
down_revision: Union[str, None] = "d267bceacfbc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE SCHEMA TODO;")
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), sa.Identity(always=False), nullable=False),
        sa.Column("task", sa.String(), nullable=False),
        sa.Column("completed_at", sa.DateTime(), nullable=True),
        sa.Column("completed_by", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("created_by", sa.String(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("updated_by", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        schema="todo",
    )


def downgrade() -> None:
    op.drop_table("items", schema="todo")
    op.execute("DROP SCHEMA TODO;")
