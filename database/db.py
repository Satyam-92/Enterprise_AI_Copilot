import psycopg2


def get_connection():
    """
    Create a PostgreSQL database connection.
    """

    connection = psycopg2.connect(
        host="localhost",
        database="enterprise_ai",
        user="postgres",
        password="********",
        port="5432"
    )

    return connection
