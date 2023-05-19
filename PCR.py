import pandas as pd
from sklearn.svm import SVC

# Load the data
data = pd.read_csv("pcr_data.csv")

# Prepare the data
data = data.dropna()
data = data.reset_index(drop=True)

# Choose an ML algorithm
clf = SVC()

# Train the ML algorithm
clf.fit(data[["CT"]], data["Label"])

# Test the ML algorithm
predictions = clf.predict(data[["CT"]])

# Evaluate the ML algorithm
accuracy = clf.score(data[["CT"]], data["Label"])

print("Accuracy:", accuracy)
