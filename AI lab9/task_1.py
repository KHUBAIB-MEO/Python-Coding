import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['flower_name'] = df['target'].apply(lambda x: iris.target_names[x])

x = df.drop(['target', 'flower_name'], axis="columns")
y = df.target

df0 = df[:50]
df1 = df[50:100]
df2 = df[100:]

plt.figure()
plt.xlabel('Sepal length')
plt.ylabel('Sepal Width')
plt.scatter(df0['sepal length (cm)'], df0['sepal width (cm)'], color="green", marker='+', label='Setosa')
plt.scatter(df1['sepal length (cm)'], df1['sepal width (cm)'], color="blue", marker='.', label='Versicolor')
plt.scatter(df2['sepal length (cm)'], df2['sepal width (cm)'], color="red", marker='*', label='Virginica')
plt.title("Sepal: Setosa vs Versicolor vs Virginica")
plt.legend()
plt.show()

plt.figure()
plt.xlabel('Petal length')
plt.ylabel('Petal Width')
plt.scatter(df0['petal length (cm)'], df0['petal width (cm)'], color="green", marker='+', label='Setosa')
plt.scatter(df1['petal length (cm)'], df1['petal width (cm)'], color="blue", marker='.', label='Versicolor')
plt.scatter(df2['petal length (cm)'], df2['petal width (cm)'], color="red", marker='*', label='Virginica')
plt.title("Petal: Setosa vs Versicolor vs Virginica")
plt.legend()
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sn.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Truth")
plt.title("Confusion Matrix")
plt.show()

new_samples = [
    [5.0, 3.4, 1.5, 0.2],
    [6.1, 2.8, 4.0, 1.3],
    [7.0, 3.2, 4.7, 1.4],
    [6.3, 3.3, 6.0, 2.5],
    [4.8, 3.0, 1.4, 0.1],
    [5.5, 2.5, 4.0, 1.3],
    [5.7, 2.8, 4.1, 1.3],
    [6.7, 3.1, 5.6, 2.4],
    [5.1, 3.8, 1.6, 0.2],
    [6.9, 3.1, 5.1, 2.3]
]

predicted_targets = knn.predict(new_samples)
predicted_names = [iris.target_names[i] for i in predicted_targets]

print("\nPredictions for 10 new samples:")
for i, sample in enumerate(new_samples):
    print(f"Sample {i+1}: {sample} => Predicted class: {predicted_names[i]}")
