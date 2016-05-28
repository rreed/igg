"""Add user table

Revision ID: 3567c18c7d44
Revises: 3075e0ac4f6a
Create Date: 2016-05-28 14:44:53.130815

"""

# revision identifiers, used by Alembic.
revision = '3567c18c7d44'
down_revision = '3075e0ac4f6a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(20), unique=True, index=True),
        sa.Column('password', sa.String(50)),
        sa.Column('email', sa.String(50), unique=True, index=True),
        sa.Column('created_at', sa.DateTime),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )

def downgrade():
    op.drop_table('users')
