"""Add site and visible to Game

Revision ID: 2ffe13aa51da
Revises: 16c498651606
Create Date: 2016-06-08 21:54:50.011757

"""

# revision identifiers, used by Alembic.
revision = '2ffe13aa51da'
down_revision = '16c498651606'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    with op.batch_alter_table("games") as batch_op:
        batch_op.add_column(sa.Column('visible', sa.Boolean))
        batch_op.add_column(sa.Column('site', sa.String))

def downgrade():
    with op.batch_alter_table("games") as batch_op:
        batch_op.drop_column('visible')
        batch_op.drop_column('site')
