"""create poll

Revision ID: 215095be422e
Revises: 45dfee8c5f46
Create Date: 2020-03-18 10:41:11.308256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '215095be422e'
down_revision = '45dfee8c5f46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('poll',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('choices', sa.ARRAY(sa.String()), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('poll')
    # ### end Alembic commands ###
