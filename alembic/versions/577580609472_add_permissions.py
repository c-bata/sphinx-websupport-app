"""add permissions

Revision ID: 577580609472
Revises: 3044c64bd8b7
Create Date: 2015-04-29 08:55:38.615000

"""

# revision identifiers, used by Alembic.
revision = '577580609472'
down_revision = '3044c64bd8b7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('userpermissions',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permissions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'permission_id')
    )
    op.drop_table('sphinx_nodes')
    op.drop_table('sphinx_commentvote')
    op.drop_table('sphinx_comments')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sphinx_comments',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('rating', sa.INTEGER(), nullable=False),
    sa.Column('time', sa.DATETIME(), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=False),
    sa.Column('displayed', sa.BOOLEAN(), nullable=True),
    sa.Column('username', sa.VARCHAR(length=64), nullable=True),
    sa.Column('proposal', sa.TEXT(), nullable=True),
    sa.Column('proposal_diff', sa.TEXT(), nullable=True),
    sa.Column('path', sa.VARCHAR(length=256), nullable=True),
    sa.Column('node_id', sa.VARCHAR(length=32), nullable=True),
    sa.ForeignKeyConstraint(['node_id'], [u'sphinx_nodes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sphinx_commentvote',
    sa.Column('username', sa.VARCHAR(length=64), nullable=False),
    sa.Column('comment_id', sa.INTEGER(), nullable=False),
    sa.Column('value', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['comment_id'], [u'sphinx_comments.id'], ),
    sa.PrimaryKeyConstraint('username', 'comment_id')
    )
    op.create_table('sphinx_nodes',
    sa.Column('id', sa.VARCHAR(length=32), nullable=False),
    sa.Column('document', sa.VARCHAR(length=256), nullable=False),
    sa.Column('source', sa.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('userpermissions')
    op.drop_table('permissions')
    ### end Alembic commands ###
