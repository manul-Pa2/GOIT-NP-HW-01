from sklearn.decomposition import PCA

pca = PCA(n_components=2, random_state=42)
X_2d = pca.fit_transform(X_scaled)

viz = pd.DataFrame({
    "pc1": X_2d[:,0],
    "pc2": X_2d[:,1],
    "true": df["species"],
    "cluster": y_pred.astype(str)
})

plt.figure(figsize=(7,4))
sns.scatterplot(data=viz, x="pc1", y="pc2", hue="true")
plt.title("PCA: справжні класи")
plt.show()

plt.figure(figsize=(7,4))               # сподіваюсь не буде помилкою зміна всього одного параметра у рівнянні
sns.scatterplot(data=viz, x="pc1", y="pc2", hue="cluster")
plt.title("PCA: кластери SpectralClustering")
plt.show()

#  Можлива не точність, але для PCA - часткова втрата данних є нормою (і результати іноді трошки відрізняються)
