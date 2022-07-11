"""empty message

Revision ID: d19c6cb9df21
Revises: 59b510bb7dd2
Create Date: 2022-07-10 12:06:34.788111

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "d19c6cb9df21"
down_revision = "59b510bb7dd2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("book", "title", existing_type=sa.VARCHAR(length=255), nullable=False)
    op.alter_column("book", "genre", existing_type=sa.VARCHAR(length=255), nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("book", "genre", existing_type=sa.VARCHAR(length=255), nullable=True)
    op.alter_column("book", "title", existing_type=sa.VARCHAR(length=255), nullable=True)
    # ### end Alembic commands ###
