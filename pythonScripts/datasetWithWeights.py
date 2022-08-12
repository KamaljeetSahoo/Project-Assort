
import csv
import pandas as pd
from normalize import scale
# header = ["Supplier Name","Region","Country","Function","Service","Avg. Cost","Rating","Average Delivery Time","Number of escalations","Year","Resources","w1","w2","w3","w4","w5","score"]
header = ["Supplier Name","Region","Country","Function","Service","Avg. Cost","Rating","Average Delivery Time","Number of escalations","Year","Resources","w1","w2","w3","w4","w5","score"]

df = pd.read_csv('dataset_normalized.csv')
m_c=(df['Avg. Cost'].drop_duplicates().nsmallest(2).iloc[-1])
m_r=(df['Rating'].drop_duplicates().nsmallest(2).iloc[-1])
m_d=(df['Average Delivery Time'].drop_duplicates().nsmallest(2).iloc[-1])
m_e=(df['Number of escalations'].drop_duplicates().nsmallest(2).iloc[-1])
m_re=(df['Resources'].drop_duplicates().nsmallest(2).iloc[-1])

with open('dataset.csv') as file:
    reader_obj = csv.DictReader(file)
    obj = csv.reader(file)
    next(obj)
  
    n=1
    nrow=[]
    new_rows=[]
    for row in obj:
    
        for i in range(1,7,2):
            for j in range(1,7,2):
                for k in range(1,7,2):
                    for l in range(1,7,2):
                        for m in range(1,7,2):
                           
                            nrow=row.copy()
                          
                            
                            c=float(row[5])
                            r=float(row[6])
                            d=float(row[7])
                            e=float(row[8])
                            re=float(row[10])
                            s=i+j+k+l+m
                            i=i/s
                            j=j/s
                            k=k/s
                            l=l/s
                            m=m/s
                            c=scale(m_c,c)
                            r=scale(m_r,r)
                            d=scale(m_d,d)
                            e=scale(m_e,e)
                            re=scale(m_re,re)
                            nrow.append(i/c)
                            nrow.append(j*r)
                            nrow.append(k/d)
                            nrow.append(l/e)
                            nrow.append(m/re)
                            

                            score = (i/c)+(j*r)+(k/d)+(l/e)+(m/re)
                            nrow.append(score)
                            new_rows.append(nrow)
                            
    with open('datasetScore.csv','w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(new_rows)                   
                    
                
            
        
                            
                        
                            


    #     print(row['Supplier Name'])
    #     break