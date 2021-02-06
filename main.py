import csv

rows=[]

with open("main.csv",'r') as f:
    data=csv.reader(f)
    for a in data:
        rows.append(a)

headers=rows[0]
planet_data=rows[1:]
headers[0]="row_num"

solar_planet_count={}

for row in planet_data:
    if(solar_planet_count.get(row[11])):
        solar_planet_count[row[11]]+=1
    else:
        solar_planet_count[row[11]]=1

print(solar_planet_count)

max_solar_system=max(solar_planet_count,key=solar_planet_count.get)

print("Solar system {} has maximum planets {} out of all the solar systems we have discovered so far!".format(max_solar_system, solar_planet_count[max_solar_system]))

temp_planet_data=list(planet_data)

for row in temp_planet_data:
    planet_mass=row[3]
    
    if planet_mass.lower() == "unknown":
        planet_data.remove(row)
        continue
    else:
        planet_mass_value = planet_mass.split(" ")[0]
        planet_mass_ref = planet_mass.split(" ")[1]
        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value) * 317.8
        row[3] = planet_mass_value

    planet_radius = row[7]
    if planet_radius.lower() == "unknown":
        planet_data.remove(row)
        continue
    else:
        planet_radius_value = planet_radius.split(" ")[0]
        planet_radius_ref = planet_radius.split(" ")[2]
        if planet_radius_ref == "Jupiter":
            planet_radius_value = float(planet_radius_value) * 11.2
        row[7] = planet_radius_value


print(len(planet_data))

KOI_351_planets = []
for a in planet_data:
    if max_solar_system == planet_data[11]:
        KOI_351_planets.append(planet_data)

print(len(KOI_351_planets))
print(KOI_351_planets)    

