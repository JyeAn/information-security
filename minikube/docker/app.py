from pickle import TRUE
from flask import Flask, make_response, send_from_directory
from flask_oidc import OpenIDConnect
from flask_cors import CORS
from functools import wraps
from bson.json_util import dumps
 
app = Flask(__name__)
 
app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'master',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})
 
oidc = OpenIDConnect(app)
@app.route('/logout')
def logout():
    oidc.logout()
    return "Logout!"

@app.route('/')
@oidc.require_login
def index():
    return "Hello user!"

if __name__ == '__main__':
    # app.run(port=5000, debug=TRUE) 
     app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=('./fullchain.pem', './private.key'))
