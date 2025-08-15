import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'mysql123',
        database = 'phonepe_pulse'
    )
    return connection

def create_tables():
    conn = connect_to_db()
    cursor = conn.cursor()

    # --- AGGREGATED FOLDER TABLES ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agg_transaction_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        state VARCHAR(255),
        year INT,
        quarter INT,
        from_timestamp DATETIME,
        to_timestamp DATETIME,
        transaction_name VARCHAR(255),
        instrument_type VARCHAR(255),
        count BIGINT,
        amount DOUBLE,
        year_quarter VARCHAR(255)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agg_transaction_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        from_timestamp DATETIME,
        to_timestamp DATETIME,
        transaction_name VARCHAR(255),
        instrument_type VARCHAR(255),
        count BIGINT,
        amount DOUBLE,
        year_quarter VARCHAR(255)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agg_user_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        state VARCHAR(255),
        registered_users BIGINT,
        app_opens BIGINT,
        brand VARCHAR(255),
        count BIGINT,
        percentage FLOAT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agg_user_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        registered_users BIGINT,
        app_opens BIGINT,
        brand VARCHAR(255),
        count BIGINT,
        percentage FLOAT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agg_insurance_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        state VARCHAR(255),
        year INT,
        quarter INT,
        from_timestamp DATETIME,
        to_timestamp DATETIME,
        transaction_name VARCHAR(255),
        instrument_type VARCHAR(255),
        count BIGINT,
        amount DOUBLE,
        year_quarter VARCHAR(255)   
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agg_insurance_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        from_timestamp DATETIME,
        to_timestamp DATETIME,
        transaction_name VARCHAR(255),
        instrument_type VARCHAR(255),
        count BIGINT,
        amount DOUBLE,
        year_quarter VARCHAR(255)
    )
    """)

    # --- MAP FOLDER TABLES ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS map_transaction_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        state VARCHAR(255),
        district VARCHAR(255),
        instrument_type VARCHAR(255),
        count BIGINT,
        amount DOUBLE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS map_transaction_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        state VARCHAR(255),
        instrument_type VARCHAR(255),
        count BIGINT,
        amount DOUBLE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS map_user_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        state VARCHAR(255),
        district VARCHAR(255),
        registered_users BIGINT,
        app_opens BIGINT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS map_user_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        state VARCHAR(255),
        registered_users BIGINT,
        app_opens BIGINT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS map_insurance_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        state VARCHAR(255),
        year INT,
        quarter INT,
        lat DOUBLE,
        lng DOUBLE,
        label VARCHAR(255),
        metric DOUBLE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS map_insurance_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        lat DOUBLE,
        lng DOUBLE,
        label VARCHAR(255),
        metric DOUBLE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS map_insurance_hover_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        state VARCHAR(255),
        district VARCHAR(255),
        year INT,
        quarter INT,
        type VARCHAR(255),
        count BIGINT,
        amount DOUBLE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS map_insurance_hover_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        state VARCHAR(255),
        year INT,
        quarter INT,
        type VARCHAR(255),
        count BIGINT,
        amount DOUBLE
    );
    """)

    # --- TOP FOLDER TABLES ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS top_transaction_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        state VARCHAR(255),
        level VARCHAR(255),
        year INT,
        quarter INT,
        entity VARCHAR(255),
        count BIGINT,
        amount DOUBLE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS top_transaction_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        entity VARCHAR(255),
        count BIGINT,
        amount DOUBLE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS top_user_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        state VARCHAR(255),
        level VARCHAR(255),
        year INT,
        quarter INT,
        entity VARCHAR(255),
        registeredUsers BIGINT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS top_user_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        entity VARCHAR(255),
        registeredUsers BIGINT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS top_insurance_state (
        id INT AUTO_INCREMENT PRIMARY KEY,
        state VARCHAR(255),
        level VARCHAR(255),
        year INT,
        quarter INT,
        entity VARCHAR(255),
        count BIGINT,
        amount DOUBLE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS top_insurance_country (
        id INT AUTO_INCREMENT PRIMARY KEY,
        level VARCHAR(255),
        year INT,
        quarter INT,
        entity VARCHAR(255),
        count BIGINT,
        amount DOUBLE
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()
    print("All tables created successfully.")

if __name__ == "__main__":
    create_tables()


