from flask import Blueprint


frontend_blueprint = Blueprint('frontend', __name__)


from app.frontend import views
