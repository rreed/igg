"""Fix varchar length on password

Revision ID: c4cd6daf947e
Revises: 59e33c434dbe
Create Date: 2016-08-31 21:40:24.666694

"""

# revision identifiers, used by Alembic.
revision = 'c4cd6daf947e'
down_revision = '59e33c434dbe'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_column('password')
        batch_op.add_column(sa.Column('password', sa.String(100)))

def downgrade():
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_column('password')
        batch_op.add_column(sa.Column('password', sa.String(50)))
