from flask import Flask
from config import get_config
from app.views import main_blueprint
from services.attendance import attendance_route
from services.auth import auth_route, app


def create_app():
    config_class = get_config()
    app.config.from_object(config_class)
    app.register_blueprint(main_blueprint)
    app.config['SECRET_KEY'] = "kalifa"
    app.register_blueprint(attendance_route, url_prefix='/attendance')
    app.register_blueprint(auth_route, url_prefix='/auth')
    return app

def check_db_connection(app):
    try:
        collections = db.connection[app.config['MONGODB_SETTINGS']['db']].list_collection_names()
        if not collections:
            print("No collections in database")
            return
        for collection in collections:
            document = db.connection[app.config['MONGODB_SETTINGS']['db']][collection].find_one()
            if document is None:
                print(f"No documents in collection {collection}")
            else:
                print(f"Successfully fetched document from collection {collection}: {document}")
        print("Connected to MongoDB")
    except Exception as e:
        print("Could not connect to MongoDB: " + str(e))
