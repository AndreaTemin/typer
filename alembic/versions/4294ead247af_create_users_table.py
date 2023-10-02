"""create users table

Revision ID: 4294ead247af
Revises: 
Create Date: 2023-07-12 12:00:40.622742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4294ead247af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Uuid, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.Unicode(50)),
        sa.Column('created_at', sa.DateTime(200)),
        sa.Column('updated_at', sa.DateTime(200)),
    )
    


def downgrade() -> None:
    op.drop_table('users')

