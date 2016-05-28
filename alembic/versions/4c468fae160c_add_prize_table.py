"""Add prize table

Revision ID: 4c468fae160c
Revises: c303d333811
Create Date: 2016-05-28 14:05:00.937034

"""

# revision identifiers, used by Alembic.
revision = '4c468fae160c'
down_revision = 'c303d333811'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('prizes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String()),
        sa.Column('description', sa.String()),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('visible', sa.Boolean),
        sa.Column('start', sa.DateTime(), nullable=False),
        sa.Column('end', sa.DateTime(), nullable=False),
        sa.Column('is_auction', sa.Boolean, default=False),
        sa.Column('is_giveaway', sa.Boolean, default=False),
        sa.Column('is_code', sa.Boolean, default=True),
        sa.Column('entry_cost', sa.Float()),
        sa.Column('game_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['game_id'], ['games.id'], name='fk_prize_games_game_id'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_prizes'))
    )

def downgrade():
    op.drop_table('prizes')
