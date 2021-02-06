import csv
import plotly.express as px

rows=[]

with open("main.csv",'r') as f:
    data=csv.reader(f)
    for a in data:
        rows.append(a)

headers=rows[0]
planet_data=rows[1:]

planet_type=[]
orbital_radius=[]
orbital_period=[]



for plrow in planet_data:
    planet_type.append(plrow[6])
    orbital_radius.append(plrow[8])
    orbital_period.append(plrow[9])

print(list(set(planet_type)))
""" print(orbital_period) """

suitable_planet=[]

for  data in planet_data:
    if(data[6]=='Terrestrial' or data[6]=='Super Earth'):
        suitable_planet.append(data)
        

print(len(suitable_planet))

temp=list(suitable_planet)


for data in temp:
    if(data[8].lower() == "unknown"):
       
        temp.remove(data)
      
    else:
        data[8]=float(data[8].split(' ')[0])



print(temp)       

for data in suitable_planet:
    if(data[9].split(' ')[1]=='days'):
        data[9]=float(data[9].split(' ')[0])
    else:
        data[9]=float(data[9].split(' ')[0])*365
  
radius=[]
period=[]        

for plrow in suitable_planet:
    radius.append(plrow[8])
    period.append(plrow[9])

fig=px.scatter(x=radius,y=period)
""" fig.show() """

for i in temp:
    if(float(i[8])<0.38 or float(i[8])>2):
        temp.remove(i)

print(len(suitable_planet),' ',len(temp))
        







  