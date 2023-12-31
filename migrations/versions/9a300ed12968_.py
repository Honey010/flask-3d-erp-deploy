"""empty message

Revision ID: 9a300ed12968
Revises: 609e9c8af7a5
Create Date: 2023-06-21 18:53:14.288685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a300ed12968'
down_revision = '609e9c8af7a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quote_date', sa.DateTime(timezone=True), nullable=True))
        batch_op.alter_column('created_at',
               existing_type=sa.DATE(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
        batch_op.alter_column('updated_at',
               existing_type=sa.DATE(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
        batch_op.drop_column('date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('quote', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DATE(), autoincrement=False, nullable=True))
        batch_op.alter_column('updated_at',
               existing_type=sa.DateTime(timezone=True),
               type_=sa.DATE(),
               existing_nullable=True)
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(timezone=True),
               type_=sa.DATE(),
               existing_nullable=True)
        batch_op.drop_column('quote_date')

    # ### end Alembic commands ###
