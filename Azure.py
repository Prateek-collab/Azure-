from tkinter import *
import requests
import json

root=Tk()
root.title('Azure')
root.geometry("400x400")
root.configure(background='green')
try:
	api_request= requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=2453F6A1-A264-441B-81EC-371229ABCBBC")
	api=json.loads(api_request.content)
	city=api[0]['ReportingArea']
	quality=api[0]['AQI']
	category=api[0]['Category']['Name']
except Exception as e:
	api="Please try again in sometime."

myLabel=Label(root, text=city+" Air quality " + str(quality)+" "+category, font=("Helvectica",10), background="green")
myLabel.pack()

#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=2453F6A1-A264-441B-81EC-371229ABC

root.mainloop()
