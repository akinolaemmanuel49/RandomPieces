#!/usr/bin/python
import sqlite3

from rich import print

from utils import hash_password, verify_password

DB_NAME: str = 'passman.db'


# Initialize the database.
def init_db():
    conn: sqlite3.Connection = sqlite3.connect(DB_NAME)

    sql_create_table_user: str = """
    CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER NOT NULL PRIMARY KEY,
        username CHAR(64) UNIQUE,
        password_hash CHAR(60)
    )
    """

    sql_create_table_stored_credentials: str = """
    CREATE TABLE IF NOT EXISTS credentials
    (
        id INTEGER NOT NULL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        account_name TEXT,
        username TEXT,
        password TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    """

    conn.execute(sql_create_table_user)
    conn.execute(sql_create_table_stored_credentials)

    conn.commit()
    conn.close()


# Create a new user
def create_new_user(username: str, plaintext_password: str):
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_NAME)

        # Check if username is already taken.
        sql_check_username = f"""
        SELECT username FROM users WHERE username = '{username}'
        """

        cursor = conn.execute(sql_check_username).fetchone()

        if cursor:
            conn.close()
            raise Exception('This username is already taken.')

        # Hash the password.
        password_hash: bytes = hash_password(plaintext_password)

        # Store user credentials in database.
        sql_insert_new_user = f"""
        INSERT INTO users (username, password_hash) VALUES('{username}', '{password_hash}');
        """

        conn.execute(sql_insert_new_user)
        conn.commit()
        conn.close()

    except Exception as e:
        raise e


# Confirm a user
def confirm_user(username: str, plaintext_password: str):
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_NAME)

        # Check if user exists.
        sql_check_if_user_exists = f"""
        SELECT id, username, password_hash FROM users WHERE username = '{username}'
        """

        cursor = conn.execute(sql_check_if_user_exists).fetchone()
        if not cursor:
            raise Exception('Invalid credentials.')

        # Get password hash from cursor.
        hashed_password: str = cursor[2]

        # Verify password.
        if verify_password(plaintext_password, hashed_password):
            # Get user id from cursor.
            user_id: int = cursor[0]
            return user_id

    except Exception as e:
        raise e


# Add a new credential.
def add_new_credential(user_id: int, account_name: str, username: str, password: str):
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_NAME)

        # Store new credentials in database.
        sql_insert_new_credential = f"""
        INSERT INTO credentials (user_id, account_name, username, password) VALUES ({user_id}, '{account_name}', '{username}', '{password}')
        """

        conn.execute(sql_insert_new_credential)
        conn.commit()
        conn.close()

    except Exception as e:
        raise e


# Retrieve all credentials.
def get_all_credentials(user_id: int):
    credentials = []
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_NAME)

        sql_get_all_credentials = f"""
        SELECT account_name, username, password FROM credentials
        """

        cursor = conn.execute(sql_get_all_credentials).fetchall()

        for credential in cursor:
            credentials.append(
                f"""{'[bold green]=[/bold green]'*32}\n[bold red]Account[/bold red]:  {credential[0]}\n[bold red]Username[/bold red]: {credential[1]}\n[bold red]Password[/bold red]: {credential[2]}""")

        for credential in credentials:
            print(credential)
        print('[bold green]=[/bold green]'*32)

    except Exception as e:
        raise e


# Add a new credential.
def update_a_credential(user_id: int, account_name: str, username: str, password: str):
    try:
        conn: sqlite3.Connection = sqlite3.connect(DB_NAME)

        # Store new credentials in database.
        sql_update_credential = f"""
        UPDATE credentials SET username = '{username}', password = '{password}' WHERE user_id = {user_id} AND account_name = '{account_name}'
        """

        conn.execute(sql_update_credential)
        conn.commit()
        conn.close()

    except Exception as e:
        raise e
