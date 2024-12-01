import os

SECRET_KEY = os.getenv('SECRET_KEY', 'what-could-it-be-2')

#SQLALCHEMY_DATABASE_URI = os.getenv('LOCAL_DATABASE_URL', 'sqlite:///db.sqlite3')

SQLALCHEMY_DATABASE_URI = 'postgresql://render_db_rf6j_user:NgFEfdg1VwwpuVT7lgGWaDTzupZiuqTI@dpg-ct6akf52ng1s738u4fdg-a.frankfurt-postgres.render.com/render_db_rf6j'