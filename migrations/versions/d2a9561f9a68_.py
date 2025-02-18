"""empty message

Revision ID: d2a9561f9a68
Revises: 
Create Date: 2021-03-25 03:40:43.480394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2a9561f9a68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=200), nullable=False),
    sa.Column('last_name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('birthday', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cocktail_id', sa.Integer(), nullable=False),
    sa.Column('cocktail_name', sa.String(length=250), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    op.drop_table('user')
    # ### end Alembic commands ###
