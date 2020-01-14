"""empty message

Revision ID: a0ee30c8697e
Revises: 
Create Date: 2020-01-13 19:03:27.511795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0ee30c8697e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sols')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sols',
    sa.Column('sol', sa.INTEGER(), nullable=False),
    sa.Column('average_temperature', sa.FLOAT(), nullable=True),
    sa.Column('high_temperature', sa.FLOAT(), nullable=True),
    sa.Column('low_temperature', sa.FLOAT(), nullable=True),
    sa.Column('horizontal_wind_speed', sa.FLOAT(), nullable=True),
    sa.Column('pressure', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('sol')
    )
    # ### end Alembic commands ###