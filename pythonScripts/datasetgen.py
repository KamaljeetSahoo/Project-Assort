import csv
import json
import numpy as np
import random
header = ["Supplier Name","Region","Country","Function","Service","Avg. Cost","Rating","Average Delivery Time","Number of escalations","Year","Resources"]
years=["2015","2016","2017","2018","2019","2020"]
region = ["R-1","R-2"]
data = json.load(open('data.json'))

average_cost = []

dataset=[]
for i in data['companies']:
    for j in data['services']:
        for k in years:
            row=[]
            row.append(i)
            row.append('APAC')
            row.append(random.choice(data['regions']))
            row.append('IT')
            row.append(j)
            row.append(100*(random.randint(1000,5000)))
            row.append(random.randint(70,95))
            row.append(random.randint(90,480))
            row.append(random.randint(30,300))
            row.append(k)
            row.append(random.randint(1000,10000))

            dataset.append(row)



with open('dataset.csv','w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(dataset)


