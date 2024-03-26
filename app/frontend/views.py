from app.frontend import frontend_blueprint as bp


@bp.route('/')
def index():
    return 'flask-inventory'
