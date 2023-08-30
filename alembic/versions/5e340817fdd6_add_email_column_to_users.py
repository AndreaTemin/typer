"""add email column to users

Revision ID: 5e340817fdd6
Revises: 4294ead247af
Create Date: 2023-07-16 10:54:25.363429

"""
from alembic import op
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision = '5e340817fdd6'
down_revision = '4294ead247af'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(table_name="users", column=Column("email", String(100), unique=False, nullable=True, default="test@gmail.com"))
    


def downgrade() -> None:
    op.drop_column(table_name="users", column_name="email")
    
