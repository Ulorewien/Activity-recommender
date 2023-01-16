import pandas as pd
import time
import math
import random

start_time = time.time()

data = pd.read_csv("final_data.csv")

cities = ["San Luis Potosi","Cuernavaca","Ciudad Victoria","Jiutepec","Soledad"]
alcohol_type = ["No_Alcohol_Served","Wine-Beer","Full_Bar"]
price_level = ["low","medium","high"]
cuisine_type = [""]

def HaDist(x1, y1, x2, y2):
    x1 = math.radians(x1)
    x2 = math.radians(x2)
    y1 = math.radians(y1)
    y2 = math.radians(y2)
    dx = x2 - x1
    dy = y2 - y1
    a = math.sin(dx/2)**2 + math.cos(x1)*math.cos(x2)*math.sin(dy/2)**2
    c = 2*math.asin(math.sqrt(a))
    r = 6371
    return(c * r)

def getFilters():
    city = random.choice(cities)
    alcohol = random.choice(alcohol_type)
    price = random.choice(price_level)
    rating = round(random.uniform(3.25,5), 2)
    cuisine = ""
    print(city, alcohol, price, rating, cuisine)
    return city, alcohol, price, rating, cuisine

def KNN(lat, lon, distance):
    city, alcohol, price, rating, cuisine = getFilters()
    for index, row in data.iterrows():
        if(row["city"] == city):
            print(HaDist(lat, lon, row["latitude"], row["longitude"]))
            if(HaDist(lat, lon, row["latitude"], row["longitude"]) < distance):
                print(row["name"]+", "+row["city"]+", "+row["state"])

# print(data.head())
KNN(22, -101, 20)

end_time = time.time()
print("Execution time :",round((end_time-start_time)*1000, 2), "ms.")