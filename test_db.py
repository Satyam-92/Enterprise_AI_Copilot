from database.db import get_connection, get_engine
import pandas as pd

# Test psycopg2
try:
    conn = get_connection()
    print("✅ psycopg2 Connected Successfully!")
    conn.close()
except Exception as e:
    print("❌ psycopg2 Error:", e)

# Test SQLAlchemy
try:
    engine = get_engine()
    df = pd.read_sql("SELECT * FROM books LIMIT 5;", engine)

    print("\n✅ SQLAlchemy Connected Successfully!")
    print(df)

except Exception as e:
    print("❌ SQLAlchemy Error:", e)