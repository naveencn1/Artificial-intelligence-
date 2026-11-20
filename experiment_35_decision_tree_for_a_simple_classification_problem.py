# CSA17 - Artificial Intelligence | Experiment 35 (Manual Ex. 4.5): Decision Tree for a Simple Classification Problem
# Name            : V V Naveen Kumar
# Register Number : 192321018

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

data = pd.DataFrame({
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast',
                'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong',
                'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
                'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'],
})

X = pd.get_dummies(data.drop(columns='Play'))
y = data['Play']

tree = DecisionTreeClassifier(criterion='entropy', random_state=0).fit(X, y)
print(export_text(tree, feature_names=list(X.columns)))
print("Training accuracy:", tree.score(X, y))

new = pd.DataFrame([{'Outlook': 'Sunny', 'Humidity': 'Normal', 'Wind': 'Weak'}])
new = pd.get_dummies(new).reindex(columns=X.columns, fill_value=0)
print("Play tennis when Sunny / Normal humidity / Weak wind ->", tree.predict(new)[0])


# ============================================================
# OUTPUT
# ============================================================
# |--- Outlook_Overcast <= 0.50
# |   |--- Humidity_High <= 0.50
# |   |   |--- Wind_Weak <= 0.50
# |   |   |   |--- Outlook_Rain <= 0.50
# |   |   |   |   |--- class: Yes
# |   |   |   |--- Outlook_Rain >  0.50
# |   |   |   |   |--- class: No
# |   |   |--- Wind_Weak >  0.50
# |   |   |   |--- class: Yes
# |   |--- Humidity_High >  0.50
# |   |   |--- Outlook_Rain <= 0.50
# |   |   |   |--- class: No
# |   |   |--- Outlook_Rain >  0.50
# |   |   |   |--- Wind_Strong <= 0.50
# |   |   |   |   |--- class: Yes
# |   |   |   |--- Wind_Strong >  0.50
# |   |   |   |   |--- class: No
# |--- Outlook_Overcast >  0.50
# |   |--- class: Yes
#
# Training accuracy: 1.0
# Play tennis when Sunny / Normal humidity / Weak wind -> Yes
