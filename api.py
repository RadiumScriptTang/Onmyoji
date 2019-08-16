from Opt import optimize
from  flask import request,Flask
import json


app = Flask(__name__)

@app.route('/opt',methods=["GET","POST"])
def opt():
    # if request.method == 'POST':

    # else:
    #     return "none"
    #optimize(monsterName,monsterNum,tansuo,enableChallenge,yuhun,[[0 for i in range(0,15)]]
    data = request.json
    print(data)
    monsterName = [int(i) for i in data["monsterName"]]
    monsterNum = [int(i) for i in data["monsterNum"]]
    enableChallenge = True
    if data["enableChallenge"] == "false":
        enableChallenge = False
    yuhun = int(data["yuhun"])
    tansuo = int(data["tansuo"])
    return json.dumps(optimize(monsterName,monsterNum,tansuo,enableChallenge,yuhun,[0 for i in range(0,15)]))

app.config['JSON_AS_ASCII'] = False
app.run()