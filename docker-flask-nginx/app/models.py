from flask_sqlalchemy import SQLAlchemy
from app import app

# TODO認証情報をenvに入れる
# DBを使用する
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@postgres-server:5432/blog'
db = SQLAlchemy(app)
