from database.db import get_connection


def test_connection():
    try:
        conn = get_connection()

        print("=" * 50)
        print("✅ PostgreSQL Connected Successfully!")
        print("=" * 50)

        cursor = conn.cursor()

        cursor.execute("SELECT version();")

        version = cursor.fetchone()

        print(version[0])

        cursor.close()
        conn.close()

        print("\nConnection Closed Successfully!")

    except Exception as e:
        print("=" * 50)
        print("❌ Database Connection Failed!")
        print("=" * 50)
        print(e)


if __name__ == "__main__":
    test_connection()