"""empty message

Revision ID: dd2b234ecff3
Revises: cde05f75af79
Create Date: 2022-07-16 23:47:58.928853

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "dd2b234ecff3"
down_revision = "cde05f75af79"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "author_details",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_date", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_date", sa.DateTime(timezone=True), nullable=True),
        sa.Column("birth_date", sa.Date(), nullable=True),
        sa.Column("birth_place", sa.String(length=255), nullable=True),
        sa.Column("bio", sa.String(length=4000), nullable=True),
        sa.Column("author_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["author_id"],
            ["author.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("author_details")
    # ### end Alembic commands ###
