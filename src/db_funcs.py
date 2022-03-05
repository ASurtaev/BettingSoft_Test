# using this class for test.
import sqlite3

import settings


def add_request(key, body):
    try:
        sqlite_connection = sqlite3.connect(settings.db_name)
        cursor = sqlite_connection.cursor()

        sqlite_insert_query = """INSERT INTO requests
                              (key, body, duplicates)  VALUES  (?, ?, ?)"""

        data_tuple = (key, body, 0)
        cursor.execute(sqlite_insert_query, data_tuple)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def find_request(key):
    record = None
    try:
        sqlite_connection = sqlite3.connect(settings.db_name)
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from requests WHERE key = ?"""
        cursor.execute(sqlite_select_query, (key,))
        record = cursor.fetchone()

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
        if record:
            return {'key': record[1], 'body': record[2], 'duplicates': record[3]}
        else:
            return None


def add_duplicate(key):
    try:
        sqlite_connection = sqlite3.connect(settings.db_name)
        cursor = sqlite_connection.cursor()

        sql_update_query = """Update requests set duplicates = duplicates + ? where key = ?"""
        data = (1, key)
        cursor.execute(sql_update_query, data)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def delete_request(key):
    try:
        sqlite_connection = sqlite3.connect(settings.db_name)
        cursor = sqlite_connection.cursor()

        sql_update_query = """DELETE from requests where key = ?"""
        cursor.execute(sql_update_query, (key, ))
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def get_all_requests():
    records = []
    try:
        sqlite_connection = sqlite3.connect(settings.db_name)
        cursor = sqlite_connection.cursor()

        sqlite_select_query = """SELECT * from requests"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
        return [{'key': record[1], 'body': record[2], 'duplicates': record[3]} for record in records]
