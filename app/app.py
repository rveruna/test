from .models import User
from .extensions import db, login_manager, csrf
def configure_extensions(app):
   # flask-sqlalchemy
   db.init_app(app)

   # flask-login
   login_manager.login_view = 'frontend.index'
   login_manager.refresh_view = 'frontend.index'

   @login_manager.user_loader
   def load_user(id):
      return User.query.get(id)

   login_manager.setup_app(app)

   # flask-wtf
   csrf.init_app(app)
