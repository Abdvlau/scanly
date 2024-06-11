# Import necessary modules and blueprints
from app.views import main_blueprint
from services.attendance import attendance_route
from services.auth import auth_route, app

# Function to create the Flask application
def create_app():
    # Get the configuration class
    config_class = get_config()
    # Configure the application with the configuration class
    app.config.from_object(config_class)
    # Register the main blueprint
    app.register_blueprint(main_blueprint)
    # Register the attendance blueprint with a URL prefix
    app.register_blueprint(attendance_route, url_prefix='/attendance')
    # Register the auth blueprint with a URL prefix
    app.register_blueprint(auth_route, url_prefix='/auth')
    # Return the configured application
    return app

# Function to check the database connection
def check_db_connection(app):
    try:
        # Get the list of collection names from the database
        collections = db.connection[app.config['MONGODB_SETTINGS']['db']].list_collection_names()
        # If there are no collections, print a message and return
        if not collections:
            print("No collections in database")
            return
        # Loop over each collection
        for collection in collections:
            # Try to find a document in the current collection
            document = db.connection[app.config['MONGODB_SETTINGS']['db']][collection].find_one()
            # If no document is found, print a message
            if document is None:
                print(f"No documents in collection {collection}")
            # If a document is found, print a success message
            else:
                print(f"Successfully fetched document from collection {collection}: {document}")
    # If an exception is raised while connecting to the database, print an error message
    except Exception as e:
        print("Could not connect to MongoDB: " + str(e))