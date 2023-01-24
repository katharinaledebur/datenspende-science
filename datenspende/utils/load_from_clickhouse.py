from os import environ
from clickhouse_connect import get_client
import ramda as R
from typing import TypedDict
import pandas as pd


class DBCredentials(TypedDict):
    user: str
    password: str
    database: str
    host: str
    port: int


def read_db_credentials_from_env() -> DBCredentials:
    return {
        "username": environ.get("CLICKHOUSE_USER"),
        "password": environ.get("CLICKHOUSE_PASSWORD"),
        "database": environ.get("CLICKHOUSE_DB"),
        "host": environ.get("CLICKHOUSE_HOST"),
        "port": 8123, #this port is currently necessary for connections via get_client
    }


def connect_to_db(credentials: DBCredentials):
    return get_client(**credentials)


def teardown_ch_db_connection(connection):
    connection.close()
    return connection


def query_ch_df(query: str) -> pd.DataFrame:
    try:
        conn = create_ch_db_connection()
        return conn.query_df(query)
    finally:
        teardown_ch_db_connection(conn)


create_ch_db_connection = R.pipe(read_db_credentials_from_env, connect_to_db)
