import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Retrieve database connection details from environment variables
db_host: str = os.getenv("POSTGRES_HOST", "")
db_port: str = os.getenv("POSTGRES_PORT", "")
db_name: str = os.getenv("POSTGRES_DB", "")
db_user: str = os.getenv("POSTGRES_USER", "")
db_password: str = os.getenv("POSTGRES_PASSWORD", "")

# Construct the database URL
DATABASE_URL: str = f"postgresql://{db_user}:{
    db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(DATABASE_URL, poolclass=QueuePool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_pool():
    return SessionLocal

