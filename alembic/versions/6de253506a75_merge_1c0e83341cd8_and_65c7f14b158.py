"""merge 1c0e83341cd8 and 65c7f14b158

Revision ID: 6de253506a75
Revises: 1c0e83341cd8, 65c7f14b158a
Create Date: 2022-09-15 18:19:41.238539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6de253506a75'
down_revision = ('1c0e83341cd8', '65c7f14b158a')
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
