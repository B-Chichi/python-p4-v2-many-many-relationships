"""add assignment association table

Revision ID: 4516a5616171
Revises: 359f270c98b5
Create Date: 2025-06-20 12:38:44.758817

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4516a5616171'
down_revision = '359f270c98b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_assignments_employee_id_employees')),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name=op.f('fk_assignments_project_id_projects')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employee_meetings',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('meeting_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employee_meetings_employee_id_employees')),
    sa.ForeignKeyConstraint(['meeting_id'], ['meetings.id'], name=op.f('fk_employee_meetings_meeting_id_meetings')),
    sa.PrimaryKeyConstraint('employee_id', 'meeting_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee_meetings')
    op.drop_table('assignments')
    # ### end Alembic commands ###
