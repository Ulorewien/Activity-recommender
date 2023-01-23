import pandas as pd
import time
import math
import random

start_time = time.time()

places = ["restaurants","bars","clubs","cafes"]
cities = ["San Luis Potosi","Cuernavaca","Ciudad Victoria","Jiutepec","Soledad",""]
alcohol_type = ["No_Alcohol_Served","Wine-Beer","Full_Bar",""]
smoking_area = ["none","section","not permitted","permitted","only at bar"]
price_level = ["low","medium","high",""]
cuisine_type = ["American","French","Indian","Mexican","Japanese","Chinese","Italian","Greek","Spanish",""]

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

def getFilters(place):
    filters = {}
    filters["place"] = place
    city = random.choice(cities)
    price = random.choice(price_level)
    rating = round(random.uniform(3.25,5), 2)
    filters["city"] = city
    filters["price"] = price
    filters["rating"] = rating
    if(place == "cafes" or place == "restaurants"):
        cuisine = random.choice(cuisine_type)
        filters["cuisine"] = cuisine
    if(place == "restaurants" or place == "clubs" or place == "bars"):
        alcohol = random.choice(alcohol_type)
        smoking = random.choice(smoking_area)
        filters["alcohol"] = alcohol
        filters["smoking"] = smoking
    print("Filters :",filters)
    return filters

def placeRecommender(lat, lon, distance, place):
    data = pd.read_csv(place+"_data.csv")
    filters = getFilters(place)
    rest_set = []
    for index, row in data.iterrows():
        ha_dist = HaDist(lat, lon, row["latitude"], row["longitude"])
        if(ha_dist < distance):
            if(filters["city"] == "" or filters["city"] == row["city"]):
                if(filters["price"] == "" or filters["price"] == row["price"]):
                    if(filters["rating"] == "" or filters["rating"] <= row["rating"]):
                        if("alcohol" in filters.keys() and (filters["alcohol"] == "" or filters["alcohol"] == row["alcohol"])):
                            if("smoking" in filters.keys() and (filters["smoking"] == "" or filters["smoking"] == row["smoking_area"])):
                                if("cuisine" in filters.keys() and (filters["cuisine"] == "" or filters["cuisine"] == row["Rcuisine"])):
                                    rest_set.append(index)
    if(len(rest_set) == 0):
        print("No "+place+" available for the selected filters.")
    else:
        for rest in rest_set:
            print(data.iloc[[rest]]["name"])

place = random.choice(places)
placeRecommender(22.168110, -100.964089, 10, place)

end_time = time.time()
print("Execution time :",round((end_time-start_time)*1000, 2), "ms.")