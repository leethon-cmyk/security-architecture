"""
Simple Flask Application
⚠️ This app demonstrates multiple security issues!
"""

from flask import Flask, request, jsonify
import config  # ⚠️ Importing hardcoded credentials

app = Flask(__name__)

# ⚠️ SECURITY ISSUE: Using hardcoded secret key
app.config['SECRET_KEY'] = 'my-super-secret-key-12345'

# ⚠️ SECURITY ISSUE: Debug mode enabled (should be False in production!)
app.config['DEBUG'] = True

# ⚠️ SECURITY ISSUE: Using credentials from config file
DATABASE_PASSWORD = config.DATABASE_CONFIG['password']
API_KEY = config.API_KEYS['stripe']


@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Insecure Demo API',
        'warning': 'This API has multiple security vulnerabilities!'
    })


@app.route('/api/users', methods=['GET'])
def get_users():
    """
    ⚠️ SECURITY ISSUE: No authentication required!
    """
    # In a real app, this would query a database
    return jsonify({
        'users': [
            {'id': 1, 'username': 'admin', 'email': 'admin@example.com'},
            {'id': 2, 'username': 'user', 'email': 'user@example.com'}
        ]
    })


@app.route('/api/login', methods=['POST'])
def login():
    """
    ⚠️ SECURITY ISSUE: Weak authentication, credentials in response
    """
    username = request.json.get('username')
    password = request.json.get('password')
    
    # ⚠️ SECURITY ISSUE: Hardcoded credentials comparison
    if username == config.ADMIN_USER and password == config.ADMIN_PASS:
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'api_key': config.API_KEYS['stripe']  # ⚠️ Exposing API key!
        })
    
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401


@app.route('/api/database/connect', methods=['POST'])
def connect_database():
    """
    ⚠️ SECURITY ISSUE: Exposing database credentials in API response
    """
    return jsonify({
        'status': 'connected',
        'config': config.DATABASE_CONFIG  # ⚠️ Never return credentials!
    })


@app.route('/api/admin/secrets', methods=['GET'])
def get_secrets():
    """
    ⚠️ SECURITY ISSUE: No authentication, exposing all secrets!
    """
    return jsonify({
        'api_keys': config.API_KEYS,
        'database': config.DATABASE_CONFIG,
        'jwt_secret': config.JWT_SECRET_KEY
    })


# ⚠️ SECURITY ISSUE: SQL Injection vulnerability
@app.route('/api/search', methods=['GET'])
def search_users():
    """
    Vulnerable to SQL injection (example, not actually executed)
    """
    search_term = request.args.get('q', '')
    # ⚠️ This would be vulnerable: f"SELECT * FROM users WHERE name = '{search_term}'"
    return jsonify({
        'warning': 'This endpoint is vulnerable to SQL injection!',
        'search_term': search_term
    })


if __name__ == '__main__':
    print("⚠️  WARNING: This application has intentional security vulnerabilities!")
    print("    For educational purposes only - DO NOT use in production!")
    print(f"    Debug mode: {app.config['DEBUG']}")
    print(f"    Secret key exposed: {app.config['SECRET_KEY']}")
    
    # ⚠️ SECURITY ISSUE: Running on all interfaces (0.0.0.0) with debug enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
