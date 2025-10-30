"""
Application Configuration
⚠️ SECURITY ISSUE: Hardcoded credentials - should use environment variables!
"""

# Database Configuration
DATABASE_CONFIG = {
    'host': 'prod-db.example.com',
    'port': 5432,
    'username': 'dbadmin',
    'password': 'DbP@ssw0rd2024!',  # ⚠️ NEVER hardcode passwords!
    'database': 'production_db'
}

# API Keys (hardcoded - very bad!)
API_KEYS = {
    'stripe': 'sk_live_51HxYz2K3m4n5o6p7q8r9s0t1u2v3w4x5y6z',
    'sendgrid': 'SG.abcdefghijklmnopqrstuvwxyz.1234567890',
    'aws_access': 'AKIAIOSFODNN7EXAMPLE',
    'aws_secret': 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
}

# Admin Credentials
ADMIN_USER = 'admin'
ADMIN_PASS = 'admin123'  # ⚠️ Terrible password!

# JWT Secret
JWT_SECRET_KEY = 'my-jwt-secret-key-12345'

# Redis Configuration
REDIS_HOST = 'redis.example.com'
REDIS_PASSWORD = 'redisPass2024'  # ⚠️ Another hardcoded password!

# Email Configuration
SMTP_USERNAME = 'noreply@example.com'
SMTP_PASSWORD = 'EmailPass123!'  # ⚠️ Never commit email passwords!

# Feature Flags
DEBUG_MODE = True  # ⚠️ Should be False in production!
ENABLE_LOGGING = True
LOG_LEVEL = 'DEBUG'

# Security Headers (ironically in an insecure config file)
SECURITY_HEADERS = {
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains'
}
