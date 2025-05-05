import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"China_population.txt", sep="\t")

plt.scatter(x = df.YEAR, y = df.POPULATION)
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population vs Year ")

x = df[["YEAR"]] 
y = df["POPULATION"]  

x_train, x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2 ,random_state = 51)
lr = LinearRegression()
lr.fit(x_train,y_train)
year_arr = [[2025], [2030], [2040]]
y_pred = lr.predict(year_arr)


m = lr.coef_
c = lr.intercept_
y = m * 7.10 + c

pred_df = pd.DataFrame({
    "Year": [2025, 2030, 2040],
    "Predicted_Population": y_pred
})
print(pred_df)

plt.show()