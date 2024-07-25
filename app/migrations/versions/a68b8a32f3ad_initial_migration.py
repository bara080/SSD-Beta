"""initial_migration

Revision ID: a68b8a32f3ad
Revises: None
Create Date: YYYY-MM-DD HH:MM:SS

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a68b8a32f3ad'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Dropping dependent constraints first
    op.drop_constraint('enrollment_studentid_fkey', 'enrollment', type_='foreignkey')
    op.drop_constraint('transcript_studentid_fkey', 'transcript', type_='foreignkey')
    op.drop_constraint('student_campus_studentid_fkey', 'student_campus', type_='foreignkey')

    # Dropping the tables
    op.drop_table('teaches')
    op.drop_table('student')

    # Creating the tables
    op.create_table('student',
        sa.Column('studentid', sa.String(length=9), nullable=False),
        sa.Column('lastname', sa.String(length=50), nullable=False),
        sa.Column('firstname', sa.String(length=50), nullable=False),
        sa.Column('initials', sa.String(length=3), nullable=True),
        sa.Column('dateofbirth', sa.Date(), nullable=True),
        sa.Column('gender', sa.CHAR(length=1), nullable=True),
        sa.Column('email', sa.String(length=100), nullable=True),
        sa.Column('address', sa.String(length=255), nullable=True),
        sa.Column('city', sa.String(length=100), nullable=True),
        sa.Column('state', sa.String(length=50), nullable=True),
        sa.Column('zipcode', sa.String(length=20), nullable=True),
        sa.Column('phone', sa.String(length=20), nullable=True),
        sa.Column('major', sa.String(length=128), nullable=True),
        sa.Column('advisorid', sa.String(length=6), nullable=True),
        sa.PrimaryKeyConstraint('studentid'),
        sa.ForeignKeyConstraint(['advisorid'], ['advisor.advisorid'], ondelete='SET NULL')
    )
    op.create_table('teaches',
        # Define columns for 'teaches' table here
    )

    # Re-adding the foreign key constraints
    op.create_foreign_key('enrollment_studentid_fkey', 'enrollment', 'student', ['studentid'], ['studentid'])
    op.create_foreign_key('transcript_studentid_fkey', 'transcript', 'student', ['studentid'], ['studentid'])
    op.create_foreign_key('student_campus_studentid_fkey', 'student_campus', 'student', ['studentid'], ['studentid'])

def downgrade():
    # Dropping the foreign key constraints
    op.drop_constraint('enrollment_studentid_fkey', 'enrollment', type_='foreignkey')
    op.drop_constraint('transcript_studentid_fkey', 'transcript', type_='foreignkey')
    op.drop_constraint('student_campus_studentid_fkey', 'student_campus', type_='foreignkey')

    # Dropping the tables
    op.drop_table('teaches')
    op.drop_table('student')

    # Creating the tables again
    # (You may need to include the table definitions here if needed)
