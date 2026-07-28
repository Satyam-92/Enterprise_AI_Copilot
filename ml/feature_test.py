from ml.feature_engineering import create_features

df = create_features()

print("=" * 80)
print(df[["text"]])
print("=" * 80)