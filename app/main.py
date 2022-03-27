from flask import Flask
import json
import pandas as pd

app = Flask(__name__)

def readdata(workbook):
    filename = "events.xlsx"
    data = pd.read_excel(filename,sheet_name=workbook)
    return data

@app.route("/",methods=["GET"])
def home():
    data_to_return = json.dumps({"message":"Welcome to Liverpool Analytics"})
    return data_to_return
    #return("<body>Welcome to Liverpool Analytics</body>")

@app.route("/get_liverpool_setpiece",methods=["GET"])
def get_liverpool_setpiece():
    workbook = "LP_Set_Piece"
    setpiece_data = readdata(workbook)
    goal_nogoal_list = list(setpiece_data["is_goal"])
    print(goal_nogoal_list)
    data = {"set_goal":goal_nogoal_list.count(1),
    "set_nogoal":goal_nogoal_list.count(0)}
    data_to_return = json.dumps(data)
    return data_to_return

@app.route("/get_liverpool_foul",methods=["GET"])
def get_liverpool_foul():
    data_list = []
    workbook = "LP_Fouls"
    whole_data = readdata(workbook)
    match_id_list = list(whole_data["id_odsp"])
    match_id_set_list = list(set(match_id_list))
    for match_id in match_id_set_list:
        data = {"match_id":match_id,"fouls":match_id_list.count(match_id)}
        data_list.append(data)
    print(data_list)
    data_to_return = json.dumps(data_list)
    return data_to_return

@app.route("/get_liverpool_leftfoot",methods=["GET"])
def get_liverpool_leftfoul():
    workbook = "LP_LeftFoot"
    whole_data = readdata(workbook)
    outcome_list = list(whole_data["shot_outcome"])
    data_1 = {"outcome":"On target","value":outcome_list.count(1)}
    data_2 = {"outcome":"Off target","value":outcome_list.count(2)}
    data_3 = {"outcome":"Blocked","value":outcome_list.count(3)}
    data_4 = {"outcome":"Hit the bar","value":outcome_list.count(4)}
    data_list = [data_1,data_2,data_3,data_4]
    print(data_list)
    data_to_return = json.dumps(data_list)
    return data_to_return
# 1	On target
# 2	Off target
# 3	Blocked
# 4	Hit the bar

@app.route("/get_liverpool_rightfoot",methods=["GET"])
def get_liverpool_rightfoul():
    workbook = "LP_RightFoot"
    whole_data = readdata(workbook)
    outcome_list = list(whole_data["shot_outcome"])
    data_1 = {"outcome":"On target","value":outcome_list.count(1)}
    data_2 = {"outcome":"Off target","value":outcome_list.count(2)}
    data_3 = {"outcome":"Blocked","value":outcome_list.count(3)}
    data_4 = {"outcome":"Hit the bar","value":outcome_list.count(4)}
    data_list = [data_1,data_2,data_3,data_4]
    print(data_list)
    data_to_return = json.dumps(data_list)
    return data_to_return

@app.route("/get_liverpool_flank",methods=["GET"])
def get_liverpool_flank():
    workbook = "LP_Right_Flank"
    whole_data = readdata(workbook)
    right_flank_length = len(list(whole_data["event_team"]))
    data_1 = {"flank":"Right","value":right_flank_length}
    workbook = "LP_Left_Flank"
    whole_data = readdata(workbook)
    left_flank_length = len(list(whole_data["event_team"]))
    data_2 = {"flank":"Left","value":left_flank_length}
    data_list = [data_1,data_2]
    print(data_list)
    data_to_return = json.dumps(data_list)
    return data_to_return

if __name__ == "__main__":
    app.run(port=7000,debug=True)