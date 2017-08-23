"""empty message

Revision ID: e7617035d6bc
Revises: 57568b984763
Create Date: 2017-08-15 11:38:32.574639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7617035d6bc'
down_revision = '57568b984763'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spotify',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('embedded_link', sa.String(length=256), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['admin_user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('embedded_link')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spotify')
    # ### end Alembic commands ###
