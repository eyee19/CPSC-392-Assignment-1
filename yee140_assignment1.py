#Everett Yee
#ID: 2254345
#yee140@mail.chapman.edu
#CPSC 392 Assignment 1

#Dataset: https://www.kaggle.com/usgs/earthquake-database
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap

data = pd.read_csv(r'C:\Users\Everett\Desktop\CPSC 392\database.csv') #23413 rows, 21 columns
#print(data.head())
#print(data.Magnitude.head(5))

mag = data[["Magnitude"]]
#mag.plot()
#print(data.hist(column="Magnitude", bins = 10))
#plt.savefig(r"C:\Users\Everett\Desktop\mag.png")
#print(data["Magnitude"].max()) #maximum is a 9.1 magnitude
#print(data["Magnitude"].min()) #minimum is 5.5, which makes sense since dataset is 5.5 or larger

#data["Magnitude Type"].value_counts().plot(kind='pie')
#data["Depth"].plot(xlim=-100,kind='kde')
#data["Status"].value_counts().plot(kind='pie')

#fig, ax = plt.subplots()
#earth = Basemap(ax=ax)
#earth.drawcoastlines(color='#556655', linewidth=0.5)
#ax.scatter(data["Longitude"], data["Latitude"], data["Magnitude"] ** 2, 
#           c='red', alpha=0.5, zorder=10)
#ax.set_xlabel("Earthquakes from 1965-2016")
#fig.savefig(r"C:\Users\Everett\Desktop\map.png")