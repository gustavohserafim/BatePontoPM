import mysql.connector
from os import environ


class DB:

    def __init__(self):
        config = {
            'host': environ['DB_HOST'],
            'user': environ['DB_USER'],
            'password': environ['DB_PASS'],
            'database': environ['DB_SCHEMA']
        }

        self._conn = mysql.connector.connect(**config)
        self._cur = self._conn.cursor(dictionary=True)

    def _execute(self, sql, params=None):
        """
        Executes a SQL command and returns its cursor
        "protected" method - Internal use only
        :param sql: string
        :param params: string
        :return: MySQL Connector Cursor object
        """
        cur = self._cur
        if params is not None:
            cur.execute(sql, params)
        else:
            cur.execute(sql)
        return cur

    def run_fa(self, sql):
        """
        Runs a SQL fetching all result lines
        :param sql: string
        :return: list of dicts or False
        """
        try:
            return self._execute(sql).fetchall()
        except (mysql.connector.Error, Exception) as e:
            print(e)
            return False

    def run_fr(self, sql):
        """
        Runs a SQL fetching one row
        :param sql: string
        :return: dict or False
        """
        try:
            return self._execute(sql).fetchone()
        except (mysql.connector.Error, Exception) as e:
            print(e)
            return False

    def run_fv(self, sql, value_name):
        """
        Runs a SQL fetching a value
        :param sql:
        :param value_name:
        :return: string or False
        """
        try:
            return self._execute(sql).fetchone()[value_name]
        except (mysql.connector.Error, Exception) as e:
            print(e)
            return False

    def run(self, sql):
        """
        Runs a SQL without result fetching
        Use with UPDATE or INSERT SQL commands
        :param sql: string
        :return: boolean
        """
        try:
            if type(sql) == str:
                self._execute(sql)
            elif type(sql) == list:
                for i in sql:
                    self._execute(i)
            self._conn.commit()
        except (mysql.connector.Error, Exception) as e:
            print(e)
            return False
        else:
            return True

    def insert_blob(self, sql, params):
        """
        Runs a SQL without result fetching expecting blob/bytes param
        :param
        :return
        """
        try:
            self._execute(sql, params)
            self._conn.commit()
        except (mysql.connector.Error, Exception) as e:
            print(e)
            return False
        else:
            return True
