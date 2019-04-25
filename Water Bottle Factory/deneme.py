import requests
import json
from flask import Flask, jsonify, request
from time import sleep

class deneme():
    def __init__(self):
        processlist = ["Plastic_To_Bottle", "Washing_The_Bottle", "Fill_The_Bottle",
                       "Cover_The_Bottle", "Tagging_The_Bottle", "Packaging"]
        machinelist = [
            "Bottle_Making_Machine", 
            "Bottle_Washing_Machine", 
            "Bottle_Filling_Machine",
            "Bottle_Cover_Machine", 
            "Bottle_Tagging_Machine", 
            "Bottle_Packaging_Machine"]
        
        Barcode = 123654852
        PartNo = 25042019
        sayac=0
        for x in range(0, 100):
            for i in range(0, len(processlist)):
                
                response = {"FactoryName": "Hayat Su",
                            "MachineName": machinelist[i],
                            "ProcessName": processlist[i],
                            "ProcessStartDate": "25/04/2019 14:30:28",
                            "Barcode": Barcode,
                            "ExpiryDate": "25/04/2021",
                            "PartNo": PartNo,
                            "ProcessIsSuccess": 1}
                self.ProcessSendData(response)
                #sleep(1)
            Barcode=Barcode+10
            PartNo=PartNo+100
            sayac=sayac+1
            
        


    def ProcessSendData(self, response):
        datas = json.dumps(response)
        r = requests.post('http://localhost:5000/transactions/new',headers={"Content-Type": "application/json"}, data=datas)
        print(r.status_code)
        #sleep(1)
        r = requests.get('http://localhost:5000/mine')
        print(r.status_code)

deneme()
