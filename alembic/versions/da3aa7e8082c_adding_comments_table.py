"""Adding comments table

Revision ID: da3aa7e8082c
Revises: 5583d091bebf
Create Date: 2022-06-30 12:08:37.079369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da3aa7e8082c'
down_revision = '5583d091bebf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable = False),
    sa.Column('content', sa.String(), nullable = False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    pass


def downgrade() -> None:
    op.drop_table("comments")
    pass
