# Algorithm to recommend activities to user based on preferences

# Importing packages
import pandas as pd
import time
import math
import random

start_time = time.time()    # Calculating start time of the code

# Defining filters. These filters will be made dynamic after Google api is integrated
places = ["restaurants","bars","clubs","cafes"]
cities = ["San Luis Potosi","Cuernavaca","Ciudad Victoria","Jiutepec","Soledad",""]
alcohol_type = ["No_Alcohol_Served","Wine-Beer","Full_Bar",""]
smoking_area = ["none","section","not permitted","permitted","only at bar"]
price_level = ["low","medium","high",""]
cuisine_type = ["American","French","Indian","Mexican","Japanese","Chinese","Italian","Greek","Spanish",""]

# Calculating the Haversine distance
def HaDist(x1, y1, x2, y2):
    # Converting latitutde and longitude to radians
    x1 = math.radians(x1)
    x2 = math.radians(x2)
    y1 = math.radians(y1)
    y2 = math.radians(y2)

    # Finding the difference between the latitude and longitude
    dx = x2 - x1
    dy = y2 - y1

    # Applying the Haversine formula
    a = math.sin(dx/2)**2 + math.cos(x1)*math.cos(x2)*math.sin(dy/2)**2
    c = 2*math.asin(math.sqrt(a))
    r = 6371    # Radius of the Earth
    return(c * r)

# Function to get the filters depending on the type of place
def getFilters(place):
    filters = {}    # Defining an empty dictionary
    filters["place"] = place    # Entering the type of place first (Eg: Restaurants, Clubs)

    # Generating random values for common filters and adding them to the dictionary
    city = random.choice(cities)
    price = random.choice(price_level)
    rating = round(random.uniform(3.25,5), 2)
    filters["city"] = city
    filters["price"] = price
    filters["rating"] = rating

    # Adding cuisine as a filter if restaurants or cafes are selected
    if(place == "cafes" or place == "restaurants"):
        cuisine = random.choice(cuisine_type)
        filters["cuisine"] = cuisine

    # Adding alcohol and smoking as a filter if restaurants, clubs or bars are selected
    if(place == "restaurants" or place == "clubs" or place == "bars"):
        alcohol = random.choice(alcohol_type)
        smoking = random.choice(smoking_area)
        filters["alcohol"] = alcohol
        filters["smoking"] = smoking

    print("Filters :",filters)      # Print the selected filters
    return filters

# Algorithm to recommend a place
def placeRecommender(lat, lon, distance, place):
    data = pd.read_csv(place+"_data.csv")   # Get the data
    filters = getFilters(place)     # Get the filters
    rest_set = []   # Define an array to save the results

    # For each place check the filters
    for index, row in data.iterrows():
        
        # Calculate the distance of the place from user's location
        ha_dist = HaDist(lat, lon, row["latitude"], row["longitude"])

        # If distance is within the specified radius then proceed to the next filter
        if(ha_dist < distance):
            # For each filter, check if filter exists, if filter is empty, or the filter matches the place
            # Add the index number of the place to the rest_set if all conditions are satisfied
            if(filters["city"] == "" or filters["city"] == row["city"]):
                if(filters["price"] == "" or filters["price"] == row["price"]):
                    if(filters["rating"] == "" or filters["rating"] <= row["rating"]):
                        if("alcohol" in filters.keys() and (filters["alcohol"] == "" or filters["alcohol"] == row["alcohol"])):
                            if("smoking" in filters.keys() and (filters["smoking"] == "" or filters["smoking"] == row["smoking_area"])):
                                if("cuisine" in filters.keys() and (filters["cuisine"] == "" or filters["cuisine"] == row["Rcuisine"])):
                                    rest_set.append(index)

    if(len(rest_set) == 0):
        # If no places satisfy the filters, then print statement
        print("No "+place+" available for the selected filters.")
    else:
        # Print names of the places if they satisfy all the conditions
        for rest in rest_set:
            print(data.iloc[[rest]]["name"])

place = random.choice(places)   # Choose a random type of place (Eg: Restaurants, bars, clubs, cafes)
placeRecommender(22.168110, -100.964089, 10, place)     # Run the algorithm (Static data has been chosen for now)

end_time = time.time()      # Calculate the end time of the code
print("Execution time :",round((end_time-start_time)*1000, 2), "ms.")       # Print the time taken to run the code