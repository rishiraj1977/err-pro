import csv
import pandas as pd



df=pd.read_csv("main.csv")
print(df)

print(df.head())
print(df.columns)

mass=df['planet_mass'].tolist()
print(mass[0:5])

extracted_mass=[]

for m in mass:
    
    m1=m.split(" ")[0]
    if(not m1=='Unknown'):

        extracted_mass.append(float(m1)*1.989e+30)

print(extracted_mass)

gravity=[]

""" for index in range(0,len(extracted_mass)):
    g=extracted_mass[index] """


""" df['gravity']=gravity """
