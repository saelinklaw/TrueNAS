"""Alert last_occurrence

Revision ID: f4e2434ad7f1
Revises: 17fe2353a0de
Create Date: 2019-12-19 15:02:01.421499+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4e2434ad7f1'
down_revision = '17fe2353a0de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('system_alert', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_occurrence', sa.DateTime(), nullable=True))

    op.execute("UPDATE system_alert SET last_occurrence = datetime")

    with op.batch_alter_table('system_alert', schema=None) as batch_op:
        batch_op.alter_column('last_occurrence',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('system_alert', schema=None) as batch_op:
        batch_op.drop_column('last_occurrence')

    # ### end Alembic commands ###
