from flask import *
from flask_oidc import OpenIDConnect
from flask_cors import CORS
from functools import wraps
import pymongo
from bson.json_util import dumps

app = Flask(__name__,static_folder='./static/',static_url_path='')
CORS(app)
app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': './secret/client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'master',
    'OIDC_SCOPES': ['openid', 'email'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OIDC_ID_TOKEN_COOKIE_TTL': 365 * 86400
})
oidc = OpenIDConnect(app)

myclient = pymongo.MongoClient("mongodb://root:example@140.124.182.19:27017/")
mydb = myclient["local"]
CNC1_col = mydb["CNC1"]
CNC2_col = mydb["CNC2"]
CNC3_col = mydb["CNC3"]
AGV_col = mydb["AGV"]
LASER_col = mydb["LASER"]

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if role in oidc._get_token_info(oidc.get_access_token()).get('realm_access').get('roles'):
                return func(*args, **kwargs)
            else:
                return abort(403)
        return wrapper
    return decorator

def get_roles(oidc):
    r_list = oidc._get_token_info(oidc.get_access_token()).get('realm_access').get('roles')
    r = list()
    if ( 'CNC1' in r_list ):
        r.append('CNC1')
    if ( 'CNC2' in r_list ):
        r.append('CNC2')
    if ( 'CNC3' in r_list ):
        r.append('CNC3')
    if ( 'AGV' in r_list ):
        r.append('AGV')
    if ( 'LASER' in r_list ):
        r.append('LASER')
    return r



def to_do_role(oidc):
    r_list = oidc._get_token_info(oidc.get_access_token()).get('realm_access').get('roles')
    r = list()
    if ( 'AGV to A' in r_list ):
        r.append('AGV to A')
    if ( 'AGV to B' in r_list ):
        r.append('AGV to B')
    if ( 'AGV to C' in r_list ):
        r.append('AGV to C')
    if ( 'AGV to D' in r_list ):
        r.append('AGV to D')
    if ( 'AGV ingoing material' in r_list ):
        r.append('AGV ingoing material')
    if ( 'AGV outgoing material' in r_list ):
        r.append('AGV outgoing material')
    if ( 'CNC1 ingoing material' in r_list ):
        r.append('CNC1 ingoing material')
    if ( 'CNC1 outgoing material' in r_list ):
        r.append('CNC1 outgoing material')
    if ( 'CNC2 ingoing material' in r_list ):
        r.append('CNC2 ingoing material')
    if ( 'CNC2 outgoing material' in r_list ):
        r.append('CNC2 outgoing material')
    if ( 'CNC3 ingoing material' in r_list ):
        r.append('CNC3 ingoing material')
    if ( 'CNC3 outgoing material' in r_list ):
        r.append('CNC3 outgoing material')
    return r
