"""merge 3e6a0d427d9c and cdbd433a9d78

Revision ID: 570b47eb43e5
Revises: 3e6a0d427d9c, cdbd433a9d78
Create Date: 2017-02-06 18:07:21.950624

"""

# revision identifiers, used by Alembic.
revision = '570b47eb43e5'
down_revision = ('3e6a0d427d9c', 'cdbd433a9d78')
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    pass


def downgrade():
    pass
