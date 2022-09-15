"""hashed_password added to table user

Revision ID: 3f86f2858a1f
Revises: d57ca36f1d9f
Create Date: 2022-09-14 22:42:29.004386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f86f2858a1f'
down_revision = 'd57ca36f1d9f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hashed_password', sa.String(length=100)))


def downgrade() -> None:
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('user', 'hashed_password')
