# Evaluation
test_loss, test_acc = cnn_model.evaluate(X_test, y_test)
print(f"CNN Accuracy: {test_acc}")
