from init import *

@app.route("/")
@oidc.require_login
def index():
    return render_template("index.html",username=oidc.user_getinfo(['name']).get('name'),
    navlist=get_roles(oidc),
    to_do_list=to_do_role(oidc))

@app.route("/CNC1")
@oidc.require_login
@require_role(role = "CNC1")
def CNC1_page():
    return render_template("CNC1.html",username=oidc.user_getinfo(['name']).get('name'),
    navlist=get_roles(oidc),
    to_do_list=to_do_role(oidc))

@app.route("/CNC2")
@oidc.require_login
@require_role(role = "CNC2")
def CNC2_page():
    return render_template("CNC2.html",username=oidc.user_getinfo(['name']).get('name'),
    navlist=get_roles(oidc),
    to_do_list=to_do_role(oidc))

@app.route("/CNC3")
@oidc.require_login
@require_role(role = "CNC3")
def CNC3_page():
    return render_template("CNC3.html",username=oidc.user_getinfo(['name']).get('name'),
    navlist=get_roles(oidc),
    to_do_list=to_do_role(oidc))

@app.route("/AGV")
@oidc.require_login
@require_role(role = "AGV")
def AGV_page():
    return render_template("AGV.html",username=oidc.user_getinfo(['name']).get('name'),
    navlist=get_roles(oidc),
    to_do_list=to_do_role(oidc))

@app.route("/LASER")
@oidc.require_login
@require_role(role = "LASER")
def LASER_page():
    return render_template("LASER.html",username=oidc.user_getinfo(['name']).get('name'),
    navlist=get_roles(oidc),
    to_do_list=to_do_role(oidc))

@app.route("/get_CNC1")
@oidc.require_login
@require_role(role = "CNC1")
def get_CNC1():
    return dumps(list(CNC1_col.find()))

@app.route("/get_CNC2")
@oidc.require_login
@require_role(role = "CNC2")
def get_CNC2():
    return dumps(list(CNC2_col.find()))

@app.route("/get_CNC3")
@oidc.require_login
@require_role(role = "CNC3")
def get_CNC3():
    return dumps(list(CNC3_col.find()))

@app.route("/get_AGV")
@oidc.require_login
@require_role(role = "AGV")
def get_AGV():
    return dumps(list(AGV_col.find()))

@app.route("/get_LASER")
@oidc.require_login
@require_role(role = "LASER")
def get_LASER():
    return dumps(list(LASER_col.find()))

@app.route("/CNC1_update", methods=['POST'])
def CNC1_update():
    try:
        new = {}
        new["$set"] = request.get_json() 
        CNC1_col.update_one({"_id":{"$exists":True}}, new)
        return "update success"
    except:
        return "update error"

@app.route("/CNC2_update", methods=['POST'])
def CNC2_update():
    try:
        new = {}
        new["$set"] = request.get_json() 
        CNC2_col.update_one({"_id":{"$exists":True}}, new)
        return "update success"
    except:
        return "update error"

@app.route("/CNC3_update", methods=['POST'])
def CNC3_update():
    try:
        new = {}
        new["$set"] = request.get_json() 
        CNC3_col.update_one({"_id":{"$exists":True}}, new)
        return "update success"
    except:
        return "update error"

@app.route("/AGV_update", methods=['POST'])
def AGV_update():
    try:
        new = {}
        new["$set"] = request.get_json() 
        AGV_col.update_one({"_id":{"$exists":True}}, new)
        return "update success"
    except:
        return "update error"

@app.route("/LASER_update", methods=['POST'])
def LASER_update():
    try:
        new = {}
        new["$set"] = request.get_json() 
        LASER_col.update_one({"_id":{"$exists":True}}, new)
        return "update success"
    except:
        return "update error"
    

app.run(host='0.0.0.0', ssl_context=('fullchain.pem', 'private.key'))
