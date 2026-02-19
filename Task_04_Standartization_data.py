from sklearn.preprocessing import StandardScaler

X = df[iris.feature_names].to_numpy()
y_true = df["target"].to_numpy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# я ще бачив реалізацію через pipe.fit() - але в нашому випадку не треба виводити в ручку кожну "х" та "у"
