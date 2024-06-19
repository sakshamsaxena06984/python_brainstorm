from sklearn.metrics import roc_auc_score

# True binary labels
y_true = [0, 0, 1, 1]

# Scores assigned by the classifier (can be probabilities or confidence scores)
y_scores = [0.1, 0.4, 0.35, 0.8]

# Compute ROC AUC
auc = roc_auc_score(y_true, y_scores)
print('ROC AUC score:', auc)
