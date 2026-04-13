from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Generate data
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)

# ❌ WRONG: scaling before split (data leakage)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print(train_acc, test_acc)





from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

# Split first
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

# Cross-validation
scores = cross_val_score(pipeline, X_train, y_train, cv=5)

print("CV Mean:", np.mean(scores))
print("CV Std:", np.std(scores))

# Final evaluation
pipeline.fit(X_train, y_train)
test_acc = pipeline.score(X_test, y_test)

print("Test Accuracy:", test_acc)





from sklearn.tree import DecisionTreeClassifier
import pandas as pd

depths = [1, 5, 20]
results = []

for d in depths:
    model = DecisionTreeClassifier(max_depth=d, random_state=42)
    model.fit(X_train, y_train)
    
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    
    results.append([d, train_acc, test_acc])

df = pd.DataFrame(results, columns=["Depth", "Train Accuracy", "Test Accuracy"])
print(df)