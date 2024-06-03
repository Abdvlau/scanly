# Importing the create_app function from your create_app module
from app.create_app import create_app

# Creating a new Flask application by calling the create_app function
app = create_app()

# Checking if this script is the main entry point of your application
if __name__ == '__main__':
    # Running the Flask development server with debug mode enabled
    app.run(debug=True)