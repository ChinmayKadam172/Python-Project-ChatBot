import requests
import json
from tkinter import *
from tkinter.ttk import Combobox

window = Tk()

# Window Config
window.title('COVID19 Vaccine Information')
window.geometry('1000x600')


def get_vaccine():
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict'
    district_id = txt1.get()
    date = txt2.get()

    parameters = {
        "district_id" : district_id,
        "date" : date
    }
    response = requests.request("GET",url,params= parameters)

    #Get Data from API and store in json
    data = json.loads(response.text)
    list_item = data["sessions"][0]
    
    myscroll = Scrollbar(window) 
    myscroll.grid(row = 3,column = 2,sticky = E, rowspan= 10)


    mylist = Listbox(window,width=100, yscrollcommand = myscroll.set )  
    for line in range(0, len(data["sessions"])): 
        mylist.insert(END, str(data["sessions"][line])) 
    mylist.grid(row = 3,column= 1,sticky = E, rowspan= 10 )    
 
    myscroll.config(command = mylist.yview) 
    


    # # Create displaybox
    # lbl_output = Label(window, textvariable=list_item)
    # lbl_output.grid(column=0,columnspan=2, row=4, sticky=W)
    # btn = Button(window, text='Get Vaccine Information', command=next_list)
    # btn.grid(column=4,row=4, sticky=W)

    covid_msg = data["sessions"][0]["name"]

    # Return covid msg to gui
    output_text.set(covid_msg)

# Create Label
lbl = Label(window, text='Enter District ID:')
lbl.grid(column=0, row=0, sticky=E)

# Create Entry Field
txt1 = Entry(window, width=30)
txt1.grid(column=1, row=0, sticky=W)

# Create Entry Field
txt2 = Entry(window, width=30)
txt2.grid(column=2, row=0,padx = 20, sticky=W)

# Create Button
btn = Button(window, text='Get Vaccine Information', command=get_vaccine)
btn.grid(column=3,row=0, sticky=W)

# Display Output
output_text = StringVar()
lbl_output = Label(window, textvariable=output_text)
lbl_output.grid(column=0,columnspan=2, row=1, sticky=W)
window.mainloop()