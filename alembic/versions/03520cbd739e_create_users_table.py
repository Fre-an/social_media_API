"""create users table

Revision ID: 03520cbd739e
Revises: d082959b6101
Create Date: 2022-06-29 12:33:31.554643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03520cbd739e'
down_revision = 'd082959b6101'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
                    sa.Column("email", sa.String(), nullable=False, unique=True),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
