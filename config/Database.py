import traceback
import psycopg2


class Database:
    def __init__(self, table):
        self.__conn = None
        self.__table = table

    def setConection(self):
        self.__conn = psycopg2.connect(
            user="postgres",
            password="root",
            host="localhost",
            port="5432",
            database="vendas",
        )

    def closeConection(self):
        if self.__conn:
            self.__conn.close()

    def execute(self, query, values=None):
        try:
            cursor = self.__conn.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            self.__conn.commit()
            return cursor.rowcount
        except (Exception, psycopg2.Error) as error:
            print(error)
            self.__conn.rollback()
        finally:
            cursor.close()
            self.closeConection()

    def findAll(self, columns="*") -> list:
        try:
            self.setConection()
            cursor = self.__conn.cursor()
            cursor.execute(f"SELECT {columns} FROM {self.__table}")
            return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            cursor.close()
            self.closeConection()

    def findBy(self, field, value, columns="*") -> list:

        try:
            self.setConection()
            cursor = self.__conn.cursor()
            cursor.execute(
                f"SELECT {columns} FROM {self.__table} WHERE {field} = {value}"
            )
            return cursor.fetchone()
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            cursor.close()
            self.closeConection()

    def insert(self, obj) -> int:
        self.setConection()
        columns = ", ".join(obj.keys())
        values = ", ".join(
            [
                f"'{value}'" if isinstance(value, str) else str(value)
                for value in obj.values()
            ]
        )
        return self.execute(f"INSERT INTO {self.__table} ({columns}) VALUES ({values})")

    def update(self, obj, field, value) -> int:
        self.setConection()
        values = ", ".join(
            [
                f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}"
                for key, value in obj.items()
            ]
        )
        return self.execute(
            f"UPDATE {self.__table} SET {values} WHERE {field} = {value}"
        )

    def delete(self, field, value) -> int:
        self.setConection()
        return self.execute(f"DELETE FROM {self.__table} WHERE {field} = {value}")