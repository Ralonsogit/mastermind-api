# App config
SECRET_KEY='12345'

PROPAGATE_EXCEPTIONS = True

# Database configuration
DEBUG = False
TESTING = False
#CSRF_ENABLED = True
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:12345@localhost:5432/mastermind'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

ERROR_404_HELP = False
