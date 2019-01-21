from flask import render_template, Blueprint
from datetime import datetime


blog = Blueprint('blog', __name__)


@blog.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


#@blog.route('/blog')
def blog_posts():
    return render_template('static_site/blog.html')
