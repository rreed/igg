"""Add buzz to game

Revision ID: 59e33c434dbe
Revises: 377f1831d276
Create Date: 2016-06-25 17:41:31.192381

"""

# revision identifiers, used by Alembic.
revision = '59e33c434dbe'
down_revision = '377f1831d276'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    with op.batch_alter_table("games") as batch_op:
        batch_op.add_column(sa.Column('buzz', sa.Float(precision=2), default=0.00))

def downgrade():
    with op.batch_alter_table("games") as batch_op:
        batch_op.drop_column('buzz')
