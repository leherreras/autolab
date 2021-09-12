from app import login_manager
from models.user import User


@login_manager.request_loader
def api_auth(request):
    api_key = request.headers.get('X-API-KEY')
    if api_key:
        user = User.query.filter(User.api_key == api_key).first()
    else:
        user = None

    return user
