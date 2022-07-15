"""empty message

Revision ID: 235f0e7b7cfe
Revises: d19c6cb9df21
Create Date: 2022-07-15 12:05:05.924587

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "235f0e7b7cfe"
down_revision = "d19c6cb9df21"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("author", sa.Column("updated_date", sa.DateTime(timezone=True), nullable=True))
    op.add_column("book", sa.Column("updated_date", sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("book", "updated_date")
    op.drop_column("author", "updated_date")
    # ### end Alembic commands ###
