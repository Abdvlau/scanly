# Importing the os module to interact with the operating system
import os

# Defining a base configuration class
class Config:
    # Getting the secret key from environment variables, default to 'default_secret_key' if not found
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    # Setting MongoDB settings, getting the host from environment variables
    MONGODB_SETTINGS = {
        'db': 'scanly',
        'host': os.environ.get("MONGODB_URI", "mongodb://localhost:27017/scanly")
    }
    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
        MONGODB_SETTINGS = {
            'db': 'scanly',
            'host': os.environ.get("MONGODB_URI", "mongodb://localhost:27017/scanly")
        }

    class DevelopmentConfig(Config):
        DEBUG = True

    class ProductionConfig(Config):
        DEBUG = False

    def get_config():
        env = os.environ.get('FLASK_ENV', 'development')
        if env == 'production':
            return ProductionConfig
        return DevelopmentConfig
# Defining a configuration class for development environment, inheriting from the base configuration class
class DevelopmentConfig(Config):
    # Enabling debug mode
    DEBUG = True

# Defining a configuration class for production environment, inheriting from the base configuration class
class ProductionConfig(Config):
    # Disabling debug mode
    DEBUG = False

# Function to get the correct configuration class based on the environment
def get_config():
    # Getting the environment from environment variables, defaulting to 'development' if not found
    env = os.environ.get('FLASK_ENV', 'development')
    # Returning the production configuration class if the environment is 'production'
    if env == 'production':
        return ProductionConfig
    # Returning the development configuration class otherwise
    return DevelopmentConfig