import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn

data = {
    'Height in (cms)': [158, 158, 160, 160, 163, 163, 160, 163, 165, 165, 165, 165, 168, 168, 168, 170, 170, 170],
    'Weight in (kgs)': [59, 59, 63, 59, 60, 60, 61, 64, 64, 61, 62, 65, 62, 63, 66, 63, 64, 68],
    'T-Shirt (Size)': ['M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']
}
df = pd.DataFrame(data)

X = df[['Height in (cms)', 'Weight in (kgs)']]
y = df['T-Shirt (Size)']

df_m = df[df['T-Shirt (Size)'] == 'M']
df_l = df[df['T-Shirt (Size)'] == 'L']

plt.figure()
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.scatter(df_m['Height in (cms)'], df_m['Weight in (kgs)'], color="green", marker='+', label='Size M')
plt.scatter(df_l['Height in (cms)'], df_l['Weight in (kgs)'], color="blue", marker='.', label='Size L')
plt.title("Customer Measurements: Size M vs Size L")
plt.legend()
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(7, 5))
sn.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Truth")
plt.title("Confusion Matrix")
plt.show()

new_customers = [
    [159, 58],
    [164, 64],
    [171, 61]
]

predicted_sizes = knn.predict(new_customers)

print("\nPredictions for new customers:")
print(f"Ahmed (159cm, 58kg): {predicted_sizes[0]}")
print(f"Yasir (164cm, 64kg): {predicted_sizes[1]}")
print(f"Rahim (171cm, 61kg): {predicted_sizes[2]}")