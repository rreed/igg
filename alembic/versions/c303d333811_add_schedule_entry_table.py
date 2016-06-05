"""Add schedule entry table

Revision ID: c303d333811
Revises: 564649ec8212
Create Date: 2016-05-28 13:57:49.024681

"""

# revision identifiers, used by Alembic.
revision = 'c303d333811'
down_revision = '564649ec8212'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('schedule_entries',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('start', sa.DateTime(), nullable=False),
        sa.Column('end', sa.DateTime(), nullable=False),
        sa.Column('title', sa.String()),
        sa.Column('description', sa.String()),
        sa.Column('visible', sa.Boolean),
        sa.Column('game_id', sa.Integer, nullable=False),
        sa.Column('interview_id', sa.Integer),
        # intentionally contrived so I can remind myself how to add them later. :)
        # sa.Column('raffle_id', sa.Integer),
        sa.Column('developer', sa.String()),
        sa.ForeignKeyConstraint(['game_id'], ['games.id'], name='fk_schedule_entry_games_game_id'),
        sa.ForeignKeyConstraint(['interview_id'], ['interviews.id'], name='fk_schedule_entry_interviews_interview_id'),
        # sa.ForeignKeyConstraint(['raffle_id'], ['raffle.id'], name='fk_schedule_entry_raffles_raffle_id'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_schedule_entries'))
    )

def downgrade():
    op.drop_table('schedule_entries')
