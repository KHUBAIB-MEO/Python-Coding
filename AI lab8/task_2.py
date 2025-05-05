import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"Observation.txt", sep="\t")

plt.scatter(x = df.Temperature, y = df.Yield)
plt.xlabel("Temperature")
plt.ylabel("Yield")
plt.title("Yield vs Temperature ")

x = df[["Temperature"]]  # input: feature
y = df["Yield"]          # output: target

x_train, x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2 ,random_state = 51)
lr = LinearRegression()
lr.fit(x_train,y_train)

y_pred = lr.predict(x_test)


m = lr.coef_
c = lr.intercept_
y = m * 7.10 + c

temp_new = float(input("Enter the temperature: "))
lr.predict([[temp_new]])

print(pd.DataFrame(np.c_[x_test,y_test,y_pred],columns=["Temperature","original_Yield","predicted_Yield"]))
plt.show()