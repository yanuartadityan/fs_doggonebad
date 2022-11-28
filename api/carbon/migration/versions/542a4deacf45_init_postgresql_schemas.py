"""init postgresql schemas

Revision ID: 542a4deacf45
Revises: 
Create Date: 2022-11-29 00:48:39.092221

"""
from alembic import op
import sqlalchemy as sa
import ormar


# revision identifiers, used by Alembic.
revision = '542a4deacf45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
    sa.Column('group_name', sa.String(length=128), nullable=False),
    sa.Column('is_max_reached', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid')
    )
    op.create_table('mode_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
    sa.Column('company_name', sa.String(length=128), nullable=False),
    sa.Column('company_reg', sa.String(length=128), nullable=False),
    sa.Column('contact_number', sa.String(length=128), nullable=False),
    sa.Column('contact_email', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid')
    )
    op.create_table('platform_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stop_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('uid'),
    sa.UniqueConstraint('username')
    )
    op.create_table('vehtype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bus',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
    sa.Column('reg_num', sa.String(length=64), nullable=False),
    sa.Column('chassis_num', sa.String(length=64), nullable=False),
    sa.Column('max_capacity', sa.Integer(), nullable=False),
    sa.Column('production_date', sa.DateTime(), nullable=True),
    sa.Column('next_service_date', sa.DateTime(), nullable=True),
    sa.Column('overhaul_date', sa.DateTime(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['vehtype.id'], name='fk_bus_vehtype_id_class_id'),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], name='fk_bus_owner_id_owner_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('initial', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('gps_lat', sa.Float(), nullable=False),
    sa.Column('gps_lon', sa.Float(), nullable=False),
    sa.Column('is_edge', sa.Boolean(), nullable=True),
    sa.Column('is_atm', sa.Boolean(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['type'], ['stop_type.id'], name='fk_stops_stop_type_id_type'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tram',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
    sa.Column('reg_num', sa.String(length=64), nullable=False),
    sa.Column('max_capacity', sa.Integer(), nullable=False),
    sa.Column('production_date', sa.DateTime(), nullable=True),
    sa.Column('next_service_date', sa.DateTime(), nullable=True),
    sa.Column('overhaul_date', sa.DateTime(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['vehtype.id'], name='fk_tram_vehtype_id_class_id'),
    sa.ForeignKeyConstraint(['owner_id'], ['owner.id'], name='fk_tram_owner_id_owner_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group', sa.Integer(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group'], ['group.id'], name='fk_users_groups_group_group_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user'], ['user.id'], name='fk_users_groups_user_user_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('platform',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('initial', sa.String(length=64), nullable=False),
    sa.Column('is_disabled_friendly', sa.Boolean(), nullable=True),
    sa.Column('is_canopy', sa.Boolean(), nullable=True),
    sa.Column('stop_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['stop_id'], ['stops.id'], name='fk_platform_stops_id_stop_id'),
    sa.ForeignKeyConstraint(['type'], ['platform_type.id'], name='fk_platform_platform_type_id_type'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('drive',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=True),
    sa.Column('start_stop', sa.Integer(), nullable=True),
    sa.Column('end_stop', sa.Integer(), nullable=True),
    sa.Column('start_platform', sa.Integer(), nullable=True),
    sa.Column('end_platform', sa.Integer(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['end_platform'], ['platform.id'], name='fk_drive_platform_id_end_platform'),
    sa.ForeignKeyConstraint(['end_stop'], ['stops.id'], name='fk_drive_stops_id_end_stop'),
    sa.ForeignKeyConstraint(['start_platform'], ['platform.id'], name='fk_drive_platform_id_start_platform'),
    sa.ForeignKeyConstraint(['start_stop'], ['stops.id'], name='fk_drive_stops_id_start_stop'),
    sa.ForeignKeyConstraint(['type'], ['mode_type.id'], name='fk_drive_mode_type_id_type'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uid')
    )
    op.create_table('stint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('platform_from', sa.Integer(), nullable=True),
    sa.Column('platform_to', sa.Integer(), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['platform_from'], ['platform.id'], name='fk_stint_platform_id_platform_from'),
    sa.ForeignKeyConstraint(['platform_to'], ['platform.id'], name='fk_stint_platform_id_platform_to'),
    sa.ForeignKeyConstraint(['type'], ['mode_type.id'], name='fk_stint_mode_type_id_type'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stint')
    op.drop_table('drive')
    op.drop_table('platform')
    op.drop_table('users_groups')
    op.drop_table('tram')
    op.drop_table('stops')
    op.drop_table('bus')
    op.drop_table('vehtype')
    op.drop_table('user')
    op.drop_table('stop_type')
    op.drop_table('platform_type')
    op.drop_table('owner')
    op.drop_table('mode_type')
    op.drop_table('group')
    # ### end Alembic commands ###