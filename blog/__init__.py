from flask import Flask, render_template
from .config.variables import SECRET_KEY


def create_app():
    app = Flask(__name__)

    # CONFIG
    app.config['SECRET_KEY'] = SECRET_KEY

    # BLUEPRINT
    from .views.admin_auth import admin
    app.register_blueprint(admin, url_prefix='/owner')

    # ERROR HANDLING IN ROUTES
    # 404
    @app.errorhandler(404)
    def errorhandler(error):
        print("404 ERROR:", str(error))
        return render_template("error-404.html")

    # 500
    @app.errorhandler(Exception)
    def errorhandler(error):
        print("500 ERROR:", str(error))
        return render_template("error-500.html")

    return app
