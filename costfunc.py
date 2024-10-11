import numpy as np
import matplotlib.pyplot as mpl

def compute_model_output(x,w,b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w*x[i] + b

    return f_wb

x_train=np.array([1.0,2.0])
y_train=np.array([300.0,500.0])
w=100
b=100
tmp_f_wb = compute_model_output(x_train,w,b)

mpl.plot(x_train,tmp_f_wb,c='blue',label='Our Prediction')
mpl.scatter(x_train,y_train,marker='x',label='Actual Values')
#it creates a scatter plot, which plots data points using cartesian coordinates.

mpl.title("Housing Prices")
mpl.ylabel('Price in 1000s of dollars')
mpl.xlabel('Size of House(1000 sqft.)')
mpl.legend()
#It's a key for your plot. It helps you identify which lines/markers correspond to which datasets.

mpl.show()
