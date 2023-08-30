"""create table words

Revision ID: 801d090fa40b
Revises: 5e340817fdd6
Create Date: 2023-08-30 09:02:05.454119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '801d090fa40b'
down_revision = '5e340817fdd6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "words",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("word", sa.String(), nullable=False),
        sa.Column("language", sa.String(), nullable=False),
        sa.Column("meaning", sa.String()),
        sa.Column("example", sa.String()),
        sa.Column("frequency", sa.Integer(), nullable=False, default=0),  # Add frequency column
        sa.UniqueConstraint("word", "language", name="uq_word_language")  # Add unique constraint
    )


def downgrade() -> None:
    op.drop_table("words")
    
