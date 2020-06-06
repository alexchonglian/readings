"""followers

Revision ID: 45dfee8c5f46
Revises: 4594a4228a15
Create Date: 2020-03-17 16:55:12.744567

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45dfee8c5f46'
down_revision = '4594a4228a15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
