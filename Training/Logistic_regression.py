from sklearn.model_selection import train_test_split
import pandas as pd

# Load dataset
data = pd.read_csv('network_data.csv')
X = data.drop('os_label', axis=1)
y = data['os_label']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training
log_model.fit(X_train, y_train)
