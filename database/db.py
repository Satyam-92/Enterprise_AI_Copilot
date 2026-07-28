import psycopg2
from sqlalchemy import create_engine


# PostgreSQL Configuration
HOST = "localhost"
DATABASE = "enterprise_ai"
USER = "postgres"
PASSWORD = "Satyam@11"
PORT = "5432"


# psycopg2 Connection
def get_connection():
    """
    Returns a psycopg2 connection.
    Used for INSERT, UPDATE, DELETE operations.
    """
    return psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT
    )


# SQLAlchemy Engine
def get_engine():
    """
    Returns a SQLAlchemy engine.
    Used for Pandas read_sql().
    """
    DATABASE_URL = (
        f"postgresql+psycopg2://{USER}:{PASSWORD.replace('@', '%40')}@{HOST}:{PORT}/{DATABASE}"
    )

    engine = create_engine(DATABASE_URL)

    return engine