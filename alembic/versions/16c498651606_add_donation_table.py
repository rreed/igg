"""Add donation table

Revision ID: 16c498651606
Revises: 1546047704bd
Create Date: 2016-06-08 19:38:15.679718

"""

# revision identifiers, used by Alembic.
revision = '16c498651606'
down_revision = '1546047704bd'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('donations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String()),
        sa.Column('url', sa.String()),
        sa.Column('twitter', sa.String()),
        sa.Column('comment', sa.String()),
        sa.Column('amount', sa.Float(precision=2)),
        sa.Column('prize_interest', sa.Boolean),
        sa.Column('time', sa.DateTime()),
        sa.Column('time_approved', sa.DateTime()),
        sa.Column('approved', sa.Boolean),
        sa.Column('ipn_hash', sa.String()),
        sa.Column('user_id', sa.Integer),
        sa.Column('prize_id', sa.Integer),
        sa.Column('challenge_id', sa.Integer),
        sa.Column('game_id', sa.Integer),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_donations_users_user_id'),
        sa.ForeignKeyConstraint(['prize_id'], ['prizes.id'], name='fk_donations_prizes_prize_id'),
        sa.ForeignKeyConstraint(['challenge_id'], ['challenges.id'], name='fk_donations_challenges_challenge_id'),
        sa.ForeignKeyConstraint(['game_id'], ['games.id'], name='fk_donations_games_game_id'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_donations'))
    )

def downgrade():
    op.drop_table('donations')
