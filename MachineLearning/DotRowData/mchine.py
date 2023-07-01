import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("MachineLearning/DotRowData/iris.csv")

print(data)

plt.figure(figsize=(150,6))
plt.plot(data['Id'], data['SepalLengthCm'],data['SepalWidthCm'],
         data['PetalLengthCm'],data['PetalWidthCm'],data,['Species'])

plt.title("Grafik Data")
plt.xlabel("Kolom X")
plt.ylabel("Kolom Y")
plt.show()

