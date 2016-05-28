"""Add prize fk to schedule

Revision ID: 3075e0ac4f6a
Revises: 4c468fae160c
Create Date: 2016-05-28 14:17:36.992285

"""

# revision identifiers, used by Alembic.
revision = '3075e0ac4f6a'
down_revision = '4c468fae160c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    with op.batch_alter_table("schedule_entries") as batch_op:
        batch_op.add_column(sa.Column('prize_id', sa.Integer))
        batch_op.create_foreign_key('fk_schedule_entry_prizes_prize_id', 'prizes', ['prize_id'], ['id'])

def downgrade():
    with op.batch_alter_table("schedule_entries") as batch_op:
        batch_op.drop_column(sa.Column('prize_id', sa.Integer))
