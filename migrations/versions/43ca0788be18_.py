"""empty message

Revision ID: 43ca0788be18
Revises: e86805c680aa
Create Date: 2021-06-26 07:23:55.127776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43ca0788be18'
down_revision = 'e86805c680aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('first_gen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=3), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('last_name'),
    sa.UniqueConstraint('last_name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('second_gen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('second_gen_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('age', sa.String(length=3), nullable=False),
    sa.ForeignKeyConstraint(['second_gen_id'], ['first_gen.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('last_name'),
    sa.UniqueConstraint('last_name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('third_gen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('third_gen_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('age', sa.String(length=3), nullable=False),
    sa.ForeignKeyConstraint(['third_gen_id'], ['second_gen.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('third_gen')
    op.drop_table('second_gen')
    op.drop_table('first_gen')
    # ### end Alembic commands ###