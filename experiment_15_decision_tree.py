# CSA17 - Artificial Intelligence | Experiment 15 (Manual Ex. 2.5): Decision Tree
# Name            : V V Naveen Kumar
# Register Number : 192321018

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("Accuracy: %.4f" % accuracy_score(y_test, pred))
print("\nDecision tree rules:")
print(export_text(model, feature_names=list(iris.feature_names)))
sample = [[5.1, 3.5, 1.4, 0.2]]
print("Prediction for", sample, "->", iris.target_names[model.predict(sample)[0]])


# ============================================================
# OUTPUT
# ============================================================
# Accuracy: 0.9778
#
# Decision tree rules:
# |--- petal length (cm) <= 2.45
# |   |--- class: 0
# |--- petal length (cm) >  2.45
# |   |--- petal length (cm) <= 4.75
# |   |   |--- petal width (cm) <= 1.60
# |   |   |   |--- class: 1
# |   |   |--- petal width (cm) >  1.60
# |   |   |   |--- class: 2
# |   |--- petal length (cm) >  4.75
# |   |   |--- petal length (cm) <= 5.15
# |   |   |   |--- class: 2
# |   |   |--- petal length (cm) >  5.15
# |   |   |   |--- class: 2
#
# Prediction for [[5.1, 3.5, 1.4, 0.2]] -> setosa
