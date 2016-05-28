"""Add interview table

Revision ID: 564649ec8212
Revises: 3792ebb79450
Create Date: 2016-05-28 13:39:56.706256

"""

# revision identifiers, used by Alembic.
revision = '564649ec8212'
down_revision = '3792ebb79450'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('interviews',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String()),
        sa.Column('description', sa.String()),
        sa.Column('visible', sa.Boolean),
        sa.Column('game_id', sa.Integer, nullable=False),
        sa.Column('developer', sa.String()),
        sa.ForeignKeyConstraint(['game_id'], ['games.id'], name='fk_interviews_games_game_id'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_interviews'))
    )

def downgrade():
    op.drop_table('interviews')
