from sklearn.metrics import accuracy_score

# Evaluation
y_pred = log_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Logistic Regression Accuracy: {accuracy}")
