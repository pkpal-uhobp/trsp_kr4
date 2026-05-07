"""add description to products

Revision ID: 0002_add_description
Revises: 0001_create_products
Create Date: 2026-05-07 00:00:00.000000
"""

from alembic import op
import sqlalchemy as sa

revision = "0002_add_description"
down_revision = "0001_create_products"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("products") as batch_op:
        batch_op.add_column(
            sa.Column(
                "description",
                sa.String(length=500),
                nullable=True,
            )
        )

    op.execute("UPDATE products SET description = 'No description' WHERE description IS NULL")

    with op.batch_alter_table("products") as batch_op:
        batch_op.alter_column(
            "description",
            existing_type=sa.String(length=500),
            nullable=False,
        )


def downgrade() -> None:
    with op.batch_alter_table("products") as batch_op:
        batch_op.drop_column("description")
