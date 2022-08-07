
import csv

from normalize import scale
header = ["Supplier Name","Region","Country","Function","Service","Avg. Cost","Rating","Average Delivery Time","Number of escalations","Year","Resources","w1","w2","w3","w4","w5","score"]
with open('dataset_normalized.csv') as file:
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
                          
                            nrow.append(i)
                            nrow.append(j)
                            nrow.append(k)
                            nrow.append(l)
                            nrow.append(m)
                            c=float(row[5])
                            r=float(row[6])
                            d=float(row[7])
                            e=float(row[8])
                            re=float(row[10])
                            c=scale(c)
                            r=scale(r)
                            d=scale(d)
                            e=scale(e)
                            re=scale(r)

                            score = (i/c)+(j*r)+(k/d)+(l/e)+(m/re)
                            nrow.append(score)
                            new_rows.append(nrow)
                            
    with open('datasetScore.csv','w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(new_rows)                   
                    
                
            
        
                            
                        
                            


    #     print(row['Supplier Name'])
    #     break