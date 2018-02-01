"""added ops comment field to schedule model

Revision ID: 0579ecfaf634
Revises: 570b47eb43e5
Create Date: 2017-10-05 18:35:07.960320

"""

# revision identifiers, used by Alembic.
revision = '0579ecfaf634'
down_revision = '570b47eb43e5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    with op.batch_alter_table("schedule_entries") as batch_op:
        batch_op.add_column(sa.Column('opscomment', sa.Text))



def downgrade():
    with op.batch_alter_table("schedule_entries") as batch_op:
        batch_op.drop_column('opscomment')
