"""create posts table

Revision ID: 543d8ca1ae5b
Revises: 
Create Date: 2022-10-12 11:36:48.034501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '543d8ca1ae5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
