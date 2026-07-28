from ml.preprocess import preprocess_books

df = preprocess_books()

print("=" * 60)
print("BOOK DATAFRAME")
print("=" * 60)

print(df)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())