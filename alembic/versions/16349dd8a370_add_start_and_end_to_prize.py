"""Add start and end to prize

Revision ID: 16349dd8a370
Revises: 2ffe13aa51da
Create Date: 2016-06-19 17:24:45.343577

"""

# revision identifiers, used by Alembic.
revision = '16349dd8a370'
down_revision = '2ffe13aa51da'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    with op.batch_alter_table("prizes") as batch_op:
        batch_op.add_column(sa.Column('start', sa.DateTime))
        batch_op.add_column(sa.Column('end', sa.DateTime))

def downgrade():
    with op.batch_alter_table("prizes") as batch_op:
        batch_op.drop_column('start')
        batch_op.drop_column('end')
