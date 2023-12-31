"""empty message

Revision ID: 56d91c71b10f
Revises: ad6b2a079013
Create Date: 2023-06-21 16:34:55.489889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56d91c71b10f'
down_revision = 'ad6b2a079013'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DATE(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DATE(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quote', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
