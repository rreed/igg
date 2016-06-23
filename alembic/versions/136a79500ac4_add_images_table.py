"""Add images table

Revision ID: 136a79500ac4
Revises: 16349dd8a370
Create Date: 2016-06-22 20:10:47.914606

"""

# revision identifiers, used by Alembic.
revision = '136a79500ac4'
down_revision = '16349dd8a370'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('images',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('path', sa.String()),
        sa.Column('name', sa.String()),
        sa.Column('prize_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['prize_id'], ['prizes.id'], name='fk_images_prizes_prize_id'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_images'))
    )

def downgrade():
    op.drop_table('images')
