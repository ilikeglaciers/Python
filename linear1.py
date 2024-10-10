import numpy as np
import matplotlib.pyplot as mpl

#x_train are the input featurea
#y_train are the output targets

x_train=np.array([1.0,2.0])
y_train=np.array([300.00,500.00])
print(f"x_train={x_train}")
print(f"y_train={y_train}")

m = x_train.shape[0]
n = len(x_train) 
print(f"m={m}")
print(f"n={n}")

x_i = x_train[1]
y_i = y_train[1]
print(f"x^({1}),y^({1}) = ({x_i},{y_i})")

mpl.scatter(x_train,y_train,marker='x',c='cyan')
#marker and c arguments are used to show red crosses, default is blue circular dots.

mpl.title("Housing Titles")
#name of the graph

mpl.ylabel("Price in 1000s of dollars")
#naming on y-axis

mpl.xlabel("Size in 1000sq ft.")
#naming on x-axis

mpl.show()
#displays my graph


