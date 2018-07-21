"""add description and plays to game

Revision ID: ac649b62c938
Revises: 0579ecfaf634
Create Date: 2018-04-10 16:14:55.045230

"""

# revision identifiers, used by Alembic.
revision = 'ac649b62c938'
down_revision = '0579ecfaf634'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("games") as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text))
        batch_op.add_column(sa.Column('plays', sa.Integer))




def downgrade():
    with op.batch_alter_table("games") as batch_op:
        batch_op.drop_column('description')
        batch_op.drop_column('plays')
