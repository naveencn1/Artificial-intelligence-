# CSA17 - Artificial Intelligence | Experiment 47 (Manual Ex. 5.7): Hyper-parameter Tuning for a Machine Learning Model
# Name            : V V Naveen Kumar
# Register Number : 192321018

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = load_wine(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

pipe = Pipeline([('scale', StandardScaler()), ('svm', SVC())])
param_grid = {
    'svm__kernel': ['linear', 'rbf'],
    'svm__C': [0.1, 1, 10, 100],
    'svm__gamma': ['scale', 0.01, 0.1],
}

grid = GridSearchCV(pipe, param_grid, cv=5, scoring='accuracy')
grid.fit(X_train, y_train)

print("Combinations tried :", len(grid.cv_results_['params']))
print("Best parameters :", grid.best_params_)
print("Best CV accuracy : %.4f" % grid.best_score_)
print("Test accuracy : %.4f" % grid.score(X_test, y_test))

print("\nTop 3 combinations:")
results = sorted(zip(grid.cv_results_['mean_test_score'], grid.cv_results_['params']),
                key=lambda t: -t[0])[:3]
for score, params in results:
    print(" %.4f %s" % (score, params))


# ============================================================
# OUTPUT
# ============================================================
# Combinations tried : 24
# Best parameters : {'svm__C': 1, 'svm__gamma': 'scale', 'svm__kernel': 'linear'}
# Best CV accuracy : 0.9923
# Test accuracy : 0.9556
#
# Top 3 combinations:
#  0.9923 {'svm__C': 1, 'svm__gamma': 'scale', 'svm__kernel': 'linear'}
#  0.9923 {'svm__C': 1, 'svm__gamma': 'scale', 'svm__kernel': 'rbf'}
#  0.9923 {'svm__C': 1, 'svm__gamma': 0.01, 'svm__kernel': 'linear'}
