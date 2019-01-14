import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


# Database Setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Login Configurations
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


from AtlasSwitch.core.views import core
from AtlasSwitch.portfolio.views import portfolio
from AtlasSwitch.blog.views import blog
from AtlasSwitch.users.views import users
from AtlasSwitch.employees_only.views import employees
from AtlasSwitch.admin.views import admin


app.register_blueprint(core)
app.register_blueprint(portfolio)
app.register_blueprint(blog)
app.register_blueprint(users)
app.register_blueprint(employees)
app.register_blueprint(admin)
