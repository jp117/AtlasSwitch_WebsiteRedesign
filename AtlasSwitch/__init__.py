from flask import Flask


app = Flask(__name__)


from AtlasSwitch.core.views import core
from AtlasSwitch.portfolio.views import portfolio
from AtlasSwitch.blog.views import blog
from AtlasSwitch.users.views import users


app.register_blueprint(core)
app.register_blueprint(portfolio)
app.register_blueprint(blog)
app.register_blueprint(users)
