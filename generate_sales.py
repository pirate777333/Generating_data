# Keith Galli tutorial
# Generating Mock Data with Python! (NumPy, Pandas, & Datetime Libraries)
# https://www.youtube.com/watch?v=VJBY2eVtf7o

import numpy as np
import pandas as pd
import random
import datetime
import calendar

# DICTIONARY OF PRODUCTS - KEY:[PRICE, WEIGHT]
electroinics={
    'Iphone':[700,9],
    'Android':[600,7],
    'ICharger':[100,8],
    'ACharger':[75,6],
    'EarPods':[250,8],
    'Headphones':[150,6],
    'Phone case':[50,5],
    'A battery':[10,4],
    'AA battery':[7,4],
    'AAA battery':[5,2],
    '100-Cupon':[100,10]    
    }

product_list=list(electroinics.keys())
tezine=[electroinics[i][1] for i in product_list]
cijene=[electroinics[i][0] for i in product_list]

def address_generator():
    cities=['Tokyo','Talin','San Francisco','LA','NY']
    countries=['JAP','EST','US','US','US']
    streets=['First','Second','Third','Fourth','Fifth']
    zips=[111,222,333,444,555,666]
    tezine=[10,8,6,4,2]

    ul=random.choices(streets, tezine)[0]
    idx=random.randint(0,4)
    return str(cities[idx])+', '+str(countries[idx])+', '+ul+', '+str(zips[idx])

def date_generator(val):
    days_num=calendar.monthrange(2019,val)[1]
    d=random.randint(1,days_num)
    if random.random()<0.5:
        date1=datetime.datetime(2019,val,d,12,0)
    else:
        date1=datetime.datetime(2019,val,d,20,0)
    mins=int(random.gauss(0,220))
    off=datetime.timedelta(minutes=mins)
    return date1+off
    # final_date=date1+off final_date.strftime("%m/%d/%y %H:%M")

oid=1756    
for month_value in range(1,13):
    if month_value <= 10:
        orders_num=int(random.gauss(100,20))
    if month_value == 11:
        orders_num=int(random.gauss(150,20))
    if month_value == 12:
        orders_num=int(random.gauss(200,20))

    name=calendar.month_name[month_value]
    df=pd.DataFrame(columns=['ID','Product','Price','Quantity','Date','Address'])
    i=0
    while orders_num > 0:
        product=random.choices(product_list, weights=tezine)[0]
        adresa=address_generator()
        dejt=date_generator(month_value)
        q=1
        if electroinics[product][0]>500:
            if random.random()<0.2:
                q=random.randint(1,2)
        elif electroinics[product][0]>200 and electroinics[product][0]<501:
            if random.random()<0.2:
                q=random.randint(1,3)
        elif electroinics[product][0]<201:
            if random.random()<0.5:
                q=random.randint(1,4)
        else:
            q=1
            
        df.loc[i]=[oid,product,electroinics[product][0],q,dejt,adresa]
        i+=1
        if product=='Iphone':
            if random.random()<0.2:
                extra='ICharger'
                q=1
                if electroinics[extra][0]>500:
                    if random.random()<0.2:
                        q=random.randint(1,2)
                elif electroinics[extra][0]>200 and electroinics[product][0]<501:
                    if random.random()<0.2:
                        q=random.randint(1,3)
                elif electroinics[extra][0]<201:
                    if random.random()<0.5:
                        q=random.randint(1,4)
                else:
                    q=1
                df.loc[i]=[oid, extra, electroinics[extra][0],q,dejt,adresa]
                i+=1
        oid+=1
        orders_num-=1
    df.to_csv(str(name)+'.csv',index=False)
    print(str(name))
