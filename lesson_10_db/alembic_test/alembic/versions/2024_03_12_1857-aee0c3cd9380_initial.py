"""initial

Revision ID: aee0c3cd9380
Revises: 
Create Date: 2024-03-12 18:57:26.503934

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aee0c3cd9380'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wallets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('private_key', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('next_action_time', sa.DateTime(), nullable=True),
    sa.Column('number_of_swaps', sa.Integer(), nullable=False),
    sa.Column('number_of_nft_mints', sa.Integer(), nullable=False),
    sa.Column('number_of_lending', sa.Integer(), nullable=False),
    sa.Column('number_of_liquidity_stake', sa.Integer(), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('private_key')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallets')
    # ### end Alembic commands ###
