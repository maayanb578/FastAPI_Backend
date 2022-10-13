"""add content column to posts table

Revision ID: c4365b20ff3b
Revises: 543d8ca1ae5b
Create Date: 2022-10-12 11:54:22.759507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4365b20ff3b'
down_revision = '543d8ca1ae5b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
