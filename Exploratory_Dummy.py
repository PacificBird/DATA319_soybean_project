import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load your dataset
df = pd.read_csv('soybean_csv.csv')

df = pd.get_dummies(df)

# Assume 'class_' columns are target variables and the rest are features
target_columns = [col for col in df.columns if col.startswith('class_')]
feature_columns = [col for col in df.columns if col not in target_columns]

# Separate features and target variable
X = df[feature_columns]
y = df[target_columns]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Get feature importances
feature_importances = rf_model.feature_importances_

# Create a DataFrame to display feature importances
feature_importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importances})

# Set a threshold for feature importance
threshold = 0.015

# Get features with importance above the threshold
selected_features = feature_importance_df[feature_importance_df['Importance'] > threshold]['Feature']

# Count the number of removed columns
num_removed_columns = len(X.columns) - len(selected_features)

# Filter the dataset to keep only selected features
df_filtered = df[selected_features]

# Display the filtered dataset
print("Number of removed columns:", num_removed_columns)
print(df_filtered)

df_filtered.to_csv("cleaned_dummy_dataset.csv")