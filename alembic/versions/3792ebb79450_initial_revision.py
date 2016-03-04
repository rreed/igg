"""Initial revision

Revision ID: 3792ebb79450
Revises: 
Create Date: 2016-02-08 19:25:00.056068

"""

# revision identifiers, used by Alembic.
revision = '3792ebb79450'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('games',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String()),
        sa.Column('developer', sa.String()),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_games'))
    )

def downgrade():
    op.drop_table('games')
