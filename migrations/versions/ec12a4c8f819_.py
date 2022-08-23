"""empty message

Revision ID: ec12a4c8f819
Revises: 6ce0d5ff9bad
Create Date: 2022-08-22 18:16:55.418251

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ec12a4c8f819'
down_revision = '6ce0d5ff9bad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=100), nullable=False))
    # ### end Alembic commands ###
