from flask import Flask

def create_app():
    app = Flask(__name__)

    from api import worker_api
    app.register_blueprint(worker_api)

    return app


app = create_app()


if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()
        # db.drop_all()
    # host = os.getenv('HOST')
    # port = os.getenv('PORT')
    app.run(debug=True, port=8181)