"""add crew pages table

Revision ID: 3e6a0d427d9c
Revises: c4cd6daf947e
Create Date: 2016-12-26 18:10:06.259893

"""

# revision identifiers, used by Alembic.
revision = '3e6a0d427d9c'
down_revision = 'c4cd6daf947e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('crew',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String()),
        sa.Column('developer', sa.String()),
        sa.Column('image', sa.String()),
        sa.Column('twitter', sa.String()),
        sa.Column('steam', sa.String()),
        sa.Column('favorite', sa.String()),
        sa.Column('profile', sa.Text()),
        sa.Column('order', sa.Integer),
        sa.Column('visible', sa.Boolean),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_crew'))
    )

def downgrade():
    op.drop_table('crew')
