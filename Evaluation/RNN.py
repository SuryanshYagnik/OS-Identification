# Evaluation
test_loss, test_acc = rnn_model.evaluate(X_test, y_test)
print(f"RNN Accuracy: {test_acc}")
