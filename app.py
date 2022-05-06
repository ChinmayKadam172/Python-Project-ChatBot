#imports
from unicodedata import name
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import requests
import json

app = Flask(__name__)
#create chatbot
englishBot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
# trainer = ChatterBotCorpusTrainer(englishBot)
# trainer.train("chatterbot.corpus.english") #train the chatter bot for english

def get_vaccine(district_id,date,pincode):
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict'

    parameters = {
        "district_id" : district_id,
        "date" : date
    }
    response = requests.request("GET",url,params= parameters)

    #Get Data from API and store in json
    data = json.loads(response.text)
    #list_item = data["sessions"][0]
    covid_msg = str()
    # for i in range(0,len(data["sessions"])):
    #     covid_msg += str(data["sessions"][i]["name"])
    for i in range(0,len(data["sessions"])):
        if data["sessions"][i]["pincode"] == int(pincode):
            ret_msg = data["sessions"][i]["name"] +"<br>"+ data["sessions"][i]["address"] +"<br>"+ str(data["sessions"][i]["slots"])+"<br>"+ str(data["sessions"][i]["vaccine"])
            print(ret_msg)
        else:
            continue
        return ret_msg

#define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    items = userText.split(' ')
    if items[0] == 'VaccineInfo':
        if len(items) == 1:
            return str('Getting vaccinated could save your life. COVID-19 vaccines provide strong protection against serious illness, hospitalization and death.<br>There is also some evidence that being vaccinated will make it less likely that you will pass the virus on to others, which means your decision to get the vaccine also protects those around you..More Info to be found on <a href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019" target=blank>Click Here</a>')
        else:
            did = items[1]
            date = items[2]
            pincode = items[3]
            return str(get_vaccine(did,date,pincode))
    elif items[0] == "CovidInfo":
        return str('COVID-19 is the disease caused by a new coronavirus called SARS-CoV-2.  WHO first learned of this new virus on 31 December 2019, following a report of a cluster of cases of ‘viral pneumonia’ in Wuhan, People’s Republic of China.More Info to be found on <a href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/question-and-answers-hub/q-a-detail/coronavirus-disease-covid-19" target=blank>Click Here</a>')
    else:
        userText = request.args.get('msg')
        return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run()