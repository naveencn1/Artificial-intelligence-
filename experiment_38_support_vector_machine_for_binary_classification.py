# CSA17 - Artificial Intelligence | Experiment 38 (Manual Ex. 4.8): Support Vector Machine (SVM) for Binary Classification
# Name            : V V Naveen Kumar
# Register Number : 192321018

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42, stratify=data.target)

scaler = StandardScaler().fit(X_train)
X_train, X_test = scaler.transform(X_train), scaler.transform(X_test)

for kernel in ('linear', 'rbf'):
    svm = SVC(kernel=kernel, C=1.0).fit(X_train, y_train)
    print("Kernel %-6s accuracy = %.4f" % (kernel, accuracy_score(y_test, svm.predict(X_test))))

svm = SVC(kernel='rbf', C=1.0).fit(X_train, y_train)
pred = svm.predict(X_test)
print("\nConfusion matrix:\n", confusion_matrix(y_test, pred))
print("\n", classification_report(y_test, pred, target_names=data.target_names))


# ============================================================
# OUTPUT
# ============================================================
# Kernel linear accuracy = 0.9860
# Kernel rbf    accuracy = 0.9790
#
# Confusion matrix:
#  [[52  1]
#  [ 2 88]]
#
#                precision    recall  f1-score   support
#
#    malignant       0.96      0.98      0.97        53
#       benign       0.99      0.98      0.98        90
#
#     accuracy                           0.98       143
#    macro avg       0.98      0.98      0.98       143
# weighted avg       0.98      0.98      0.98       143
