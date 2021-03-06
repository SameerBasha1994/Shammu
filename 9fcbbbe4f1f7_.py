"""empty message

Revision ID: 9fcbbbe4f1f7
Revises: 69f20665bc6e
Create Date: 2018-05-10 17:03:16.025003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9fcbbbe4f1f7'
down_revision = '69f20665bc6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_mobilenum'), 'user', ['mobilenum'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_mobilenum'), table_name='user')
    # ### end Alembic commands ###
