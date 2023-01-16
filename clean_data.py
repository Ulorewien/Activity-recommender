import pandas as pd

data = pd.read_csv("Dataset\Mexico_data\geoplaces2.csv", na_values='?')
# print(data.shape)

subset1 = data.iloc[:, [0,1,2,3,4]]
subset2 = data.iloc[:, [5,6,7,8,9]]
subset3 = data.iloc[:, [10,11,12,13,14]]
subset4 = data.iloc[:, [15,16,17,18,19,20]]

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

final_data = data.drop(["the_geom_meter","fax","accessibility","zip","url","Rambience","franchise","area","other_services"], axis=1)
final_data["country"] = final_data["country"].fillna("Mexico")
final_data = final_data.dropna(subset=["city","state"])
final_data["city"] = final_data["city"].replace("san luis potosi","San Luis Potosi")
final_data["city"] = final_data["city"].replace("s.l.p","San Luis Potosi")
final_data["city"] = final_data["city"].replace("san luis potos","San Luis Potosi")
final_data["city"] = final_data["city"].replace("slp","San Luis Potosi")
final_data["city"] = final_data["city"].replace("s.l.p.","San Luis Potosi")
final_data["city"] = final_data["city"].replace("san luis potosi ","San Luis Potosi")
final_data["city"] = final_data["city"].replace("victoria","Ciudad Victoria")
final_data["city"] = final_data["city"].replace("victoria ","Ciudad Victoria")
final_data["city"] = final_data["city"].replace("Cd Victoria","Ciudad Victoria")
final_data["city"] = final_data["city"].replace("Cd. Victoria","Ciudad Victoria")
final_data["city"] = final_data["city"].replace("cuernavaca","Cuernavaca")
final_data["state"] = final_data["state"].replace("San Luis Potosi","SLP")
final_data["state"] = final_data["state"].replace("san luis potosi","SLP")
final_data["state"] = final_data["state"].replace("slp","SLP")
final_data["state"] = final_data["state"].replace("S.L.P.","SLP")
final_data["state"] = final_data["state"].replace("s.l.p.","SLP")
final_data["state"] = final_data["state"].replace("san luis potos","SLP")
final_data["state"] = final_data["state"].replace("morelos","Morelos")
final_data["state"] = final_data["state"].replace("tamaulipas","Tamaulipas")
final_data["country"] = final_data["country"].replace("mexico","Mexico")
# print(final_data.head())
# print(final_data.isnull().sum())

final_data.to_csv("final_data.csv", index=False)