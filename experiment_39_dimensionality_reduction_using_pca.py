# CSA17 - Artificial Intelligence | Experiment 39 (Manual Ex. 4.9): Dimensionality Reduction using PCA
# Name            : V V Naveen Kumar
# Register Number : 192321018

import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X = StandardScaler().fit_transform(iris.data)
print("Original shape:", X.shape)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("Reduced shape :", X_pca.shape)
print("Explained variance ratio:", np.round(pca.explained_variance_ratio_, 4))
print("Total variance retained : %.2f%%" % (100 * pca.explained_variance_ratio_.sum()))
print("\nPrincipal components (rows) vs features:")
print(np.round(pca.components_, 3))
print("\nFirst 5 samples in PCA space:")
print(np.round(X_pca[:5], 3))

# Optional visualisation
# import matplotlib.pyplot as plt
# plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target); plt.xlabel('PC1'); plt.ylabel('PC2'); plt.show()


# ============================================================
# OUTPUT
# ============================================================
# Original shape: (150, 4)
# Reduced shape : (150, 2)
# Explained variance ratio: [0.7296 0.2285]
# Total variance retained : 95.81%
#
# Principal components (rows) vs features:
# [[ 0.521 -0.269  0.58   0.565]
#  [ 0.377  0.923  0.024  0.067]]
#
# First 5 samples in PCA space:
# [[-2.265  0.48 ]
#  [-2.081 -0.674]
#  [-2.364 -0.342]
#  [-2.299 -0.597]
#  [-2.39   0.647]]
