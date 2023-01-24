from datenspende.utils import create_ch_db_connection, teardown_ch_db_connection, query_ch_df
import pandas as pd


def test_query_df_returns_df():
    df = query_ch_df(
        "select * from datenspende_derivatives.homogenized_features LIMIT 10;"
    )

    assert len(df) == 4
    assert "type" in df.columns
