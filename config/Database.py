import traceback
import psycopg2
import os


class Database:
    def __init__(self, table):
        self.__conn = None
        self.__table = table

    def setConection(self):
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASS")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_NAME")

        self.__conn = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
        )

    def closeConection(self):
        if self.__conn:
            self.__conn.close()

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

    def find(self, fields, values, columns="*", operators=["="]) -> list:
        
        conditions = " AND ".join([f"{field} {operator} {value}" for field, operator, value in zip(fields, operators, values)])
        
        if len(fields) == 1:
            conditions = f"{fields[0]} {operators[0]} {values[0]}"
        query = f"SELECT {columns} FROM {self.__table} WHERE {conditions}"
        
        try:
            self.setConection()
            cursor = self.__conn.cursor()
            cursor.execute(
                query, values
            )
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
            print(error)
        finally:
            cursor.close()
            self.closeConection()

    def insert(self, obj, returning) -> int:
        self.setConection()
        columns = ", ".join(obj.keys())
        values = ", ".join(
            [
                f"'{value}'" if isinstance(value, str) else str(value)
                for value in obj.values()
            ]
        )

        query = f"INSERT INTO {self.__table} ({columns}) VALUES ({values}) RETURNING {returning}"

        try:
            cursor = self.__conn.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            self.__conn.commit()
            
            return cursor.fetchone()[0]
        except (Exception, psycopg2.Error) as error:
            print(error)
            self.__conn.rollback()
        finally:
            cursor.close()
            self.closeConection()

    def update(self, obj, field, value) -> int:
        self.setConection()
        values = ", ".join(
            [
                f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}"
                for key, value in obj.items()
            ]
        )

        query = f"UPDATE {self.__table} SET {values} WHERE {field} = {value}"
        
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
            
    def update_field(self, obj, where_fields, where_values) -> int:
        self.setConection()
        set_values = ", ".join(
            [
                f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}"
                for key, value in obj.items()
            ]
        )
        where_conditions = " AND ".join(
            [f"{field} = {value}" for field, value in zip(where_fields, where_values)]
        )
        query = f"UPDATE {self.__table} SET {set_values} WHERE {where_conditions}"
        
        try:
            cursor = self.__conn.cursor()
            if set_values:
                cursor.execute(query, set_values)
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

    def delete(self, field, value) -> int:
        self.setConection()
        
        query = f"DELETE FROM {self.__table} WHERE {field} = {value}"
        try:
            cursor = self.__conn.cursor()
            cursor.execute(query)
            self.__conn.commit()

            return cursor.rowcount
        except (Exception, psycopg2.Error) as error:
            print(error)
            self.__conn.rollback()
        finally:
            cursor.close()
            self.closeConection()
