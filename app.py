import json
from flask import Flask, render_template, redirect, request

app = Flask(__name__,template_folder='template',static_folder='static')
# companies = ['deloitte','cognizent']
# import view
@app.route("/")
def home():
  return render_template('index.html')

@app.route("/companies/<name>")
def companies(name):
  return render_template('jobslist.html',name=name)

@app.route("/getjobData",methods = ["POST"])
def getjobData():
  payload = request.get_json()
  # lenth = len(payload["name"])
  name = payload["name"]
  fileName = './Json_data/'+name+'/job_data.json'
  with open(fileName,'r',encoding='utf-8') as f:
    try:data = json.load(f)
    except:data={}
  f.close()
  result = {}
  for i in [*data.keys()][0:50]:
    result.update({i:data[i]})
  # print(result)
  return (result)

@app.route("/companies/<company>/<jobId>",methods = ["GET"])
def jobDetails(company,jobId):
  fileName = './Json_data/' + company + '/job_data.json'
  with open(fileName, 'r', encoding='utf-8') as f:
    try :
      data = json.load(f)[jobId]
    except:
      # print(e)
      data = {}
  # print(data)
  return render_template('jobDetails.html', jobId=json.dumps(data))

def error():
  return "404"
if __name__ == "__main__":
  app.run(debug=True)