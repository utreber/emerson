"""empty message

Revision ID: 7218d0268966
Revises: 55c5a0abb843
Create Date: 2017-08-14 18:19:30.437114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7218d0268966'
down_revision = '55c5a0abb843'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news_article', sa.Column('date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news_article', 'date')
    # ### end Alembic commands ###