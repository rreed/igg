"""add simple admin to user

Revision ID: cdbd433a9d78
Revises: c4cd6daf947e
Create Date: 2017-01-20 18:32:38.761785

"""

# revision identifiers, used by Alembic.
revision = 'cdbd433a9d78'
down_revision = 'c4cd6daf947e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("users") as batch_op:
        batch_op.add_column(sa.Column('admin', sa.Boolean))

def downgrade():
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_column('admin')

