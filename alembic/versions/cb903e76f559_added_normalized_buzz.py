"""added normalized buzz

Revision ID: cb903e76f559
Revises: ac649b62c938
Create Date: 2018-08-17 19:08:09.715882

"""

# revision identifiers, used by Alembic.
revision = 'cb903e76f559'
down_revision = 'ac649b62c938'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table('games') as batch_op:
        batch_op.add_column(sa.Column('normalized_buzz', sa.Float))

def downgrade():
    with op.batch_alter_table('games') as batch_op:
        batch_op.drop_column('normalized_buzz')
