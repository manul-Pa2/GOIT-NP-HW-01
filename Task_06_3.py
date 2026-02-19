from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

ari = adjusted_rand_score(y_true, y_pred)        # <-- ось тут вже знадобилися ті параметри))
nmi = normalized_mutual_info_score(y_true, y_pred)

ari, nmi


# точність після mapping ~ 0.85
# ARI ~ 0.65, NMI ~ 0.68
