SECRET_KEY = 'your-secret-key'
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

# Flask-Mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
# Please change your google settings before using SMTP
MAIL_USERNAME = "your-email"
MAIL_PASSWORD = "your-email-password"
