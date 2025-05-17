import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree

df = pd.read_csv("survival.csv")

inputs = df[['Pclass', 'Sex', 'Age']]
target = df['Survived']

le_sex = LabelEncoder()
inputs['sex_n'] = le_sex.fit_transform(inputs['Sex'])

inputs_n = inputs.drop('Sex', axis='columns')

x_train, x_test, y_train, y_test = train_test_split(inputs_n, target, test_size=0.2)

model = tree.DecisionTreeClassifier()
model.fit(x_train, y_train)

test_data = pd.DataFrame([
    [3, 21, 1],
    [1, 35, 0],
    [2, 30, 1],
    [3, 18, 0],
    [1, 45, 1]
], columns=['Pclass', 'Age', 'sex_n'])

predictions = model.predict(test_data)

for i, p in enumerate(predictions, 1):
    print(f"Prediction {i}: {'Survived' if p == 1 else 'Did not survive'}")

