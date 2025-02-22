"""empty message

Revision ID: 9d7d85f316b9
Revises: 0f18e71e5f3d
Create Date: 2024-02-09 10:24:57.011954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d7d85f316b9'
down_revision = '0f18e71e5f3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.drop_constraint('person_planet_id_fkey', type_='foreignkey')
        batch_op.drop_column('planet_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('person', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('person_planet_id_fkey', 'planet', ['planet_id'], ['id'])

    # ### end Alembic commands ###
