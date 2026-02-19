import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df, x="species")
plt.title("Кількість об'єктів у кожному класі")
plt.show()

# Візуалізація "фіча - клас"
plt.figure(figsize=(8,4))
sns.boxplot(data=df, x="species", y="petal length (см)")
plt.title("Розподіл petal length (см) за класами")
plt.show()

sns.pairplot(df, vars=iris.feature_names, hue="species", corner=True)      # Можливо не дуже зрозуміло, я не певен як зробити по іншому data=df у sns
plt.show()
