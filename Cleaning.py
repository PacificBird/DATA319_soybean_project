import pandas as pd

def clean(csv):
    # Load your dataset
    df = pd.read_csv(csv)

    # Display the percentage of missing values in each column
    print(df.isna().mean())

    # Capture column names before dropping
    columns_before = df.columns.tolist()

    # Calculate the corresponding integer threshold
    threshold = 0.875 * len(df)

    # Drop columns with missing values exceeding the threshold
    df = df.dropna(thresh=threshold, axis=1)
    df = df.dropna()

    # Capture column names after dropping
    columns_after = df.columns.tolist()

    # Identify deleted columns
    deleted_columns = set(columns_before) - set(columns_after)

    # Print the list of deleted columns
    print("Deleted columns:", deleted_columns)

    # Display the cleaned DataFrame
    print(df)

    # Save the modified dataset after cleaning
    df.to_csv(f'clean{csv}', index=False)

clean('soybean_csv.csv')
