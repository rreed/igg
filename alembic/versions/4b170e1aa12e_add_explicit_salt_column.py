"""Add explicit salt column

Revision ID: 4b170e1aa12e
Revises: 3567c18c7d44
Create Date: 2016-05-28 15:46:54.265729

"""

# revision identifiers, used by Alembic.
revision = '4b170e1aa12e'
down_revision = '3567c18c7d44'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    with op.batch_alter_table("users") as batch_op:
        batch_op.add_column(sa.Column('salt', sa.String))

def downgrade():
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_column('salt')
