import pandas as pd

data1 = pd.read_csv("Dataset\Mexico_data\geoplaces2.csv", na_values='?')
# print(data.shape)

subset1 = data1.iloc[:, [0,1,2,3,4]]
subset2 = data1.iloc[:, [5,6,7,8,9]]
subset3 = data1.iloc[:, [10,11,12,13,14]]
subset4 = data1.iloc[:, [15,16,17,18,19,20]]

subset1 = subset1.drop(["the_geom_meter"], axis=1)

subset2 = subset2.drop(["fax"], axis=1)
subset2["country"] = subset2["country"].fillna("Mexico")
subset2 = subset2.dropna(subset=["city","state"])
subset2["city"] = subset2["city"].replace("san luis potosi","San Luis Potosi")
subset2["city"] = subset2["city"].replace("s.l.p","San Luis Potosi")
subset2["city"] = subset2["city"].replace("san luis potos","San Luis Potosi")
subset2["city"] = subset2["city"].replace("slp","San Luis Potosi")
subset2["city"] = subset2["city"].replace("s.l.p.","San Luis Potosi")
subset2["city"] = subset2["city"].replace("san luis potosi ","San Luis Potosi")
subset2["city"] = subset2["city"].replace("victoria","Ciudad Victoria")
subset2["city"] = subset2["city"].replace("victoria ","Ciudad Victoria")
subset2["city"] = subset2["city"].replace("Cd Victoria","Ciudad Victoria")
subset2["city"] = subset2["city"].replace("Cd. Victoria","Ciudad Victoria")
subset2["city"] = subset2["city"].replace("cuernavaca","Cuernavaca")
subset2["state"] = subset2["state"].replace("San Luis Potosi","SLP")
subset2["state"] = subset2["state"].replace("san luis potosi","SLP")
subset2["state"] = subset2["state"].replace("slp","SLP")
subset2["state"] = subset2["state"].replace("S.L.P.","SLP")
subset2["state"] = subset2["state"].replace("s.l.p.","SLP")
subset2["state"] = subset2["state"].replace("san luis potos","SLP")
subset2["state"] = subset2["state"].replace("morelos","Morelos")
subset2["state"] = subset2["state"].replace("tamaulipas","Tamaulipas")
subset2["country"] = subset2["country"].replace("mexico","Mexico")

subset3 = subset3.drop(["accessibility","zip"], axis=1)

subset4 = subset4.drop(["url","Rambience","franchise","area","other_services"], axis=1)

# print(subset4["price"].value_counts())
# print(subset4.isnull().sum())

data2 = pd.read_csv("Dataset\Mexico_data\\rating_final.csv", na_values='?')
data2 = data2.drop(["userID","rating"], axis=1)
data2 = data2.groupby("placeID")[["food_rating","service_rating"]].mean()
data2["rating"] = round(data2[["food_rating","service_rating"]].mean(axis=1) + 3, 2)
data2 = data2.drop(["food_rating","service_rating"], axis=1)
# print(data2.head())

data3 = pd.read_csv("Dataset\Mexico_data\chefmozcuisine.csv", na_values='?')
data3["Rcuisine"] = data3.groupby("placeID")["Rcuisine"].transform(lambda x : ','.join(x))
data3 = data3.drop_duplicates()
# print(data3.head())
# print(data3["Rcuisine"].value_counts())

data1 = data1.drop(["the_geom_meter","fax","accessibility","zip","url","Rambience","franchise","area","other_services","dress_code"], axis=1)
data1["country"] = data1["country"].fillna("Mexico")
data1 = data1.dropna(subset=["city","state"])
data1["city"] = data1["city"].replace("san luis potosi","San Luis Potosi")
data1["city"] = data1["city"].replace("s.l.p","San Luis Potosi")
data1["city"] = data1["city"].replace("san luis potos","San Luis Potosi")
data1["city"] = data1["city"].replace("slp","San Luis Potosi")
data1["city"] = data1["city"].replace("s.l.p.","San Luis Potosi")
data1["city"] = data1["city"].replace("san luis potosi ","San Luis Potosi")
data1["city"] = data1["city"].replace("victoria","Ciudad Victoria")
data1["city"] = data1["city"].replace("victoria ","Ciudad Victoria")
data1["city"] = data1["city"].replace("Cd Victoria","Ciudad Victoria")
data1["city"] = data1["city"].replace("Cd. Victoria","Ciudad Victoria")
data1["city"] = data1["city"].replace("cuernavaca","Cuernavaca")
data1["state"] = data1["state"].replace("San Luis Potosi","SLP")
data1["state"] = data1["state"].replace("san luis potosi","SLP")
data1["state"] = data1["state"].replace("slp","SLP")
data1["state"] = data1["state"].replace("S.L.P.","SLP")
data1["state"] = data1["state"].replace("s.l.p.","SLP")
data1["state"] = data1["state"].replace("san luis potos","SLP")
data1["state"] = data1["state"].replace("morelos","Morelos")
data1["state"] = data1["state"].replace("tamaulipas","Tamaulipas")
data1["country"] = data1["country"].replace("mexico","Mexico")

data4 = pd.merge(data1, data2, on="placeID")
final_data = pd.merge(data3, data4, on="placeID", how="right")
final_data["Rcuisine"] = final_data["Rcuisine"].fillna("Others")
# print(final_data.head())
# print(final_data.isnull().sum())
# print(final_data.describe())
# print(final_data.columns)
# print(final_data.shape)

final_data.to_csv("final_data.csv", index=False)

# print(final_data["smoking_area"].value_counts())