"""Add marathon info table

Revision ID: 1546047704bd
Revises: 11d40b277d49
Create Date: 2016-06-01 19:37:07.588280

"""

# revision identifiers, used by Alembic.
revision = '1546047704bd'
down_revision = '11d40b277d49'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('marathon_info',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('total', sa.Float(), nullable=False),
        sa.Column('start', sa.DateTime(), nullable=False),
        sa.Column('hours', sa.Integer()),
        sa.Column('next_hour_cost', sa.Float()),
        sa.Column('current_game_id', sa.Integer(), nullable=False),
        sa.Column('next_game_id', sa.Integer(), nullable=False),
        sa.Column('current_schedule_entry', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['current_game_id'], ['games.id'], name='fk_marathon_info_games_current_game_id'),
        sa.ForeignKeyConstraint(['next_game_id'], ['games.id'], name='fk_marathon_info_games_next_game_id'),
        sa.ForeignKeyConstraint(['current_schedule_entry'], ['schedule_entries.id'], name='fk_marathon_info_schedule_entries_current_schedule_entry'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_marathon_info'))
    )

def downgrade():
    op.drop_table('marathon_info')
