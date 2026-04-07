import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import IsolationForest

# Loading the data from the csv file
data = pd.read_csv("logs.csv")

# Converting  text to numeric features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['log'])

# Training the  model
model = IsolationForest(contamination=0.3, random_state=42)
model.fit(X)

# Predict
data['prediction'] = model.predict(X)

# Convert output
data['result'] = data['prediction'].apply(lambda x: "Anomaly" if x == -1 else "Normal")

print(data[['log', 'result']])
