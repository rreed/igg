"""Add challenge table

Revision ID: 11d40b277d49
Revises: 4b170e1aa12e
Create Date: 2016-05-28 17:48:09.210186

"""

# revision identifiers, used by Alembic.
revision = '11d40b277d49'
down_revision = '4b170e1aa12e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('challenges',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String()),
        sa.Column('description', sa.String()),
        sa.Column('accepted', sa.Boolean, default=False),
        sa.Column('visible', sa.Boolean, default=True),
        sa.Column('bounty', sa.Float),
        sa.Column('total', sa.Float),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_interviews'))
    )

def downgrade():
    op.drop_table('challenges')
