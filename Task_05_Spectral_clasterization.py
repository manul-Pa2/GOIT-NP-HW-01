from sklearn.cluster import SpectralClustering

spec = SpectralClustering(
    n_clusters=3,
    affinity="nearest_neighbors",         # інфу по методам взяв з джерела: https://scikit-learn.ru/stable/modules/clustering.html
    n_neighbors=10,
    assign_labels="kmeans",
    random_state=42
)

y_pred = spec.fit_predict(X_scaled)
np.unique(y_pred, return_counts=True)
