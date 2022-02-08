"""1

Revision ID: 956a8ccfbd7b
Revises: 
Create Date: 2022-02-08 12:16:36.067234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '956a8ccfbd7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reference_stat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('event_type', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reference_stat_id'), 'reference_stat', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reference_stat_id'), table_name='reference_stat')
    op.drop_table('reference_stat')
    # ### end Alembic commands ###