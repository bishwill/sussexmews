import os

from sqlalchemy import create_engine, Engine

def get_engine(**kwargs) -> Engine:
    user = os.environ["DB_USER"]
    pwd = os.environ["DB_PWD"]
    host = os.environ["DB_HOST"]
    port = os.environ["DB_PORT"]
    db = os.environ["DB_NAME"]
    url = f"postgresql://{user}:{pwd}@{host}:{port}/{db}"
    return create_engine(url, **kwargs)
