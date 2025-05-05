import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"student_info.txt", sep="\t")

plt.scatter(x = df.student_marks, y = df.study_hours)
plt.xlabel("Student_Marks")
plt.ylabel("Study_Hours")
plt.title("Student_Marks vs Study_Hours")


x = df.drop("student_marks", axis = "columns")
y = df.drop("study_hours", axis = "columns")

x_train, x_test,y_train,y_test = train_test_split(x,y, test_size = 0.2 ,random_state = 51)
lr = LinearRegression()
lr.fit(x_train,y_train)
lr.coef_
lr.intercept_
y_pred = lr.predict(x_test)


m = 3.91306058
c = 50.59564059
y = m * 7.10 + c

temp_new = float(input("Enter the hour: "))
lr.predict([[temp_new]])

print(pd.DataFrame(np.c_[x_test,y_test,y_pred],columns=["study_hours","original_Marks","predicted_Marks"]))
plt.show()