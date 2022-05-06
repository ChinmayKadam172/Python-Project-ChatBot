import requests
import json
district_id = "395"
date = "31-01-2022"
parameters = {
    "district_id" : "395",
    "date" : "31-01-2022"
}
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
response = requests.request("GET",url,params= parameters)

data = json.loads(response.text)
for i in range(0,len(data["sessions"])):
    if data["sessions"][i]["vaccine"] == "COVISHIELD":
        txt = json.dumps(data["sessions"][i],sort_keys=True,indent=4)
        print(txt)



# print(response.json())

# url = ("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=" + district_id + "&date=" + date)
# response = requests.get(url)

# def jprint(obj):
#     text = json.dumps(obj, sort_keys=obj, indent=4)
#     txt = json.dumps(obj,sort_keys=True,indent=4)
#     print(txt)


# jprint(response.json())


