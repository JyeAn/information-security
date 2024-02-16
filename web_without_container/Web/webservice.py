from init import *

r = list()
r.append('CNC1')
r.append('CNC2')
r.append('CNC3')
r.append('AGV')
r.append('LASER')

@app.route("/")


def index():
    return render_template("index.html", navlist = r)

@app.route("/CNC1")

def CNC1_page():
    return render_template("CNC1.html", navlist = r)

@app.route("/CNC2")

def CNC2_page():
    return render_template("CNC2.html", navlist = r)

@app.route("/CNC3")

def CNC3_page():
    return render_template("CNC3.html", navlist = r)
@app.route("/AGV")

def AGV_page():
    return render_template("AGV.html", navlist = r)

@app.route("/LASER")

def LASER_page():
    return render_template("LASER.html", navlist = r)

@app.route("/get_CNC1")

def get_CNC1():
    return dumps(list(CNC1_col.find()))

@app.route("/get_CNC2")

def get_CNC2():
    return dumps(list(CNC2_col.find()))

@app.route("/get_CNC3")

def get_CNC3():
    return dumps(list(CNC3_col.find()))

@app.route("/get_AGV")

def get_AGV():
     
    return dumps(list(AGV_col.find()))

@app.route("/get_LASER")

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
    

app.run(debug=True, host='0.0.0.0', port=5000)
