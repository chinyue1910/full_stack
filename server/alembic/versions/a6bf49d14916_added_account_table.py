"""Added account table

Revision ID: a6bf49d14916
Revises: 
Create Date: 2022-05-26 13:16:28.069849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6bf49d14916'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False, comment='商品名稱'),
    sa.Column('description', sa.String(length=255), nullable=False, comment='商品介紹'),
    sa.Column('thumbnail', sa.String(length=50), nullable=False, comment='縮圖'),
    sa.Column('price', sa.Integer(), nullable=False, comment='價格'),
    sa.Column('storage', sa.Integer(), nullable=False, comment='存貨'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False, comment='名字'),
    sa.Column('last_name', sa.String(length=20), nullable=False, comment='姓'),
    sa.Column('email', sa.String(length=50), nullable=False, comment='信箱'),
    sa.Column('hashed_password', sa.String(length=100), nullable=False, comment='密碼'),
    sa.Column('superuser', sa.Boolean(), nullable=False, comment='管理者'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='會員'),
    sa.Column('product_id', sa.Integer(), nullable=True, comment='商品'),
    sa.Column('count', sa.Integer(), nullable=True, comment='數量'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='會員'),
    sa.Column('name', sa.String(), nullable=False, comment='收件人'),
    sa.Column('phone', sa.String(), nullable=False, comment='電話號碼'),
    sa.Column('status', sa.String(), nullable=False, comment='訂單狀態'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_detail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True, comment='訂單'),
    sa.Column('product_id', sa.Integer(), nullable=True, comment='商品'),
    sa.Column('count', sa.Integer(), nullable=False, comment='數量'),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_detail')
    op.drop_table('order')
    op.drop_table('cart')
    op.drop_table('user')
    op.drop_table('product')
    # ### end Alembic commands ###
