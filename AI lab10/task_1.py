import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree

df = pd.read_csv("salary_dataset.csv")

inputs = df.drop('Salary>80k', axis='columns')
target = df['Salary>80k']

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

inputs['company_n'] = le_company.fit_transform(inputs['Company'])
inputs['job_n'] = le_job.fit_transform(inputs['Position'])
inputs['degree_n'] = le_degree.fit_transform(inputs['Qualification'])

inputs_n = inputs.drop(['Company', 'Position', 'Qualification'], axis='columns')

x_train, x_test, y_train, y_test = train_test_split(inputs_n, target, test_size=0.2, random_state=42)

model = tree.DecisionTreeClassifier()
model.fit(x_train, y_train)

test_data = pd.DataFrame([
    [1, 2, 0],
    [2, 3, 1],
    [0, 0, 1],
    [2, 1, 0],
    [1, 1, 1]
], columns=['company_n', 'job_n', 'degree_n'])

predictions = model.predict(test_data)

for i, p in enumerate(predictions, 1):
    print(f"Prediction {i}: {p}")

