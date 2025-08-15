import mysql.connector
from datetime import datetime

def connect_to_db():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "mysql123",
        database = "phonepe_pulse"
    )
    return connection

def insert_agg_transaction_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO agg_transaction_state (
        level, state, year, quarter, from_timestamp, to_timestamp,
        transaction_name, instrument_type, count, amount, year_quarter
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "state", "year", "quarter", "from_timestamp", "to_timestamp",
        "transaction_name", "instrument_type", "count", "amount", "year_quarter"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_agg_transaction_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO agg_transaction_country (
        level, year, quarter, from_timestamp, to_timestamp,
        transaction_name, instrument_type, count, amount, year_quarter
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "from_timestamp", "to_timestamp",
        "transaction_name", "instrument_type", "count", "amount", "year_quarter"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_agg_user_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO agg_user_state(
        level, state, registered_users, app_opens,
        brand, count, percentage
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "state", "registered_users", "app_opens",
        "brand", "count", "percentage"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_agg_user_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO agg_user_country (
        level, registered_users, app_opens,
        brand, count, percentage
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "registered_users", "app_opens",
        "brand", "count", "percentage"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_agg_insurance_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO agg_insurance_state (
        level, state, year, quarter, from_timestamp, to_timestamp,
        transaction_name, instrument_type, count, amount, year_quarter
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "state", "year", "quarter", "from_timestamp", "to_timestamp",
        "transaction_name", "instrument_type", "count", "amount", "year_quarter"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_agg_insurance_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO agg_insurance_country (
        level, year, quarter, from_timestamp, to_timestamp,
        transaction_name, instrument_type, count, amount, year_quarter
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "from_timestamp", "to_timestamp",
        "transaction_name", "instrument_type", "count", "amount", "year_quarter"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_map_transaction_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO map_transaction_state (
        level, year, quarter, state, district,
        instrument_type, count, amount
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "state", "district",
        "instrument_type", "count", "amount"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_map_transaction_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()
    
    insert_query = """
    INSERT INTO map_transaction_country (
        level, year, quarter, state,
        instrument_type, count, amount
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "state",
        "instrument_type", "count", "amount"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_map_user_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO map_user_state (
        level, year, quarter, state, district,
        registered_users, app_opens
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "state", "district",
        "registered_users", "app_opens"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_map_user_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO map_user_country (
        level, year, quarter, state,
        registered_users, app_opens
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "state",
        "registered_users", "app_opens"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_map_insurance_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO map_insurance_state (
        level, state, year, quarter, lat, lng, label, metric
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "state", "year", "quarter",
        "lat", "lng", "label", "metric"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_map_insurance_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO map_insurance_country (
        level, year, quarter, lat, lng, label, metric
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "lat", "lng", "label", "metric"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_map_insurance_hover_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO map_insurance_hover_state (
        level, state, district, year, quarter,
        type, count, amount
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "state", "district", "year", "quarter",
        "type", "count", "amount"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_map_insurance_hover_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO map_insurance_hover_country (
        level, state, year, quarter,
        type, count, amount
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "state", "year", "quarter",
        "type", "count", "amount"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_top_transaction_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO top_transaction_state (
        state, level, year, quarter, entity, count, amount
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "state", "level", "year", "quarter", "entity", "count", "amount"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_top_transaction_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO top_transaction_country (
        level, year, quarter, entity, count, amount
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "entity", "count", "amount"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_top_user_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO top_user_state (
        state, level, year, quarter, entity, registeredUsers
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "state", "level", "year", "quarter", "entity", "registeredUsers"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_top_user_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO top_user_country (
        level, year, quarter, entity, registeredUsers
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "entity", "registeredUsers"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_top_insurance_state(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO top_insurance_state (
        state, level, year, quarter, entity, count, amount
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "state", "level", "year", "quarter", "entity", "count", "amount"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

def insert_top_insurance_country(df):
    conn = connect_to_db()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO top_insurance_country (
        level, year, quarter, entity, count, amount
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    data = df[[
        "level", "year", "quarter", "entity", "count", "amount"
    ]].values.tolist()

    cursor.executemany(insert_query, data)
    conn.commit()
    cursor.close()
    conn.close()

