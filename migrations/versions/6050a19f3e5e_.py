"""empty message

Revision ID: 6050a19f3e5e
Revises: 9d7d85f316b9
Create Date: 2024-02-09 10:53:18.557864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6050a19f3e5e'
down_revision = '9d7d85f316b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.drop_constraint('vehicle_person_id_fkey', type_='foreignkey')
        batch_op.drop_column('person_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('person_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('vehicle_person_id_fkey', 'person', ['person_id'], ['id'])

    # ### end Alembic commands ###
