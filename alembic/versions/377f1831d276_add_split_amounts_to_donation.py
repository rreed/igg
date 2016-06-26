"""Add split amounts to donation

Revision ID: 377f1831d276
Revises: 136a79500ac4
Create Date: 2016-06-25 17:04:37.388766

"""

# revision identifiers, used by Alembic.
revision = '377f1831d276'
down_revision = '136a79500ac4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    with op.batch_alter_table("donations") as batch_op:
        batch_op.add_column(sa.Column('amount_one', sa.Float(precision=2)))
        batch_op.add_column(sa.Column('amount_two', sa.Float(precision=2)))
        batch_op.add_column(sa.Column('amount_three', sa.Float(precision=2)))

def downgrade():
    with op.batch_alter_table("donations") as batch_op:
        batch_op.drop_column(sa.Column('amount_one'))
        batch_op.drop_column(sa.Column('amount_two'))
        batch_op.drop_column(sa.Column('amount_three'))
