"""init

Revision ID: d57ca36f1d9f
Revises: 
Create Date: 2022-09-14 21:50:11.628660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd57ca36f1d9f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False)
    )
    #op.add_column('tablename')


def downgrade() -> None:
    op.drop_table('user')
    #op.drop_column('tablename', 'columnname')
