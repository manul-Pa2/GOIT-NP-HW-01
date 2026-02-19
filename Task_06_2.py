from itertools import permutations
from sklearn.metrics import accuracy_score

best_acc = -1
best_perm = None
best_cm = None

for perm in permutations(range(3)):                 # Спочатку намагався маніпулювати "y_true/y_pred" але знайшовся спосіб параметрів best, який спрацював
    mapped = np.array([perm[i] for i in y_pred])
    acc = accuracy_score(y_true, mapped)
    if acc > best_acc:
        best_acc = acc
        best_perm = perm
        best_cm = confusion_matrix(y_true, mapped)

best_acc, best_perm, best_cm
