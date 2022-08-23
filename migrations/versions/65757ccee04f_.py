"""empty message

Revision ID: 65757ccee04f
Revises: ec12a4c8f819
Create Date: 2022-08-22 18:18:41.526697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65757ccee04f'
down_revision = 'ec12a4c8f819'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('password', sa.String(length=100), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    op.drop_table('article')
    # ### end Alembic commands ###
