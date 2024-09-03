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
            
    def insert(self, **kwargs):
        self.setConection()
        columns = ', '.join(kwargs.keys())
        values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in kwargs.values()])
        query = f"INSERT INTO {self.__table} ({columns}) VALUES ({values})"
        self.execute(query)
        return "Data inserted successfully"
            
    def findAll(self, columns="*"):
        self.setConection()
        cursor = self.__conn.cursor()
        cursor.execute(f"SELECT {columns} FROM {self.__table}")
        return cursor.fetchall()

    def findBy(self, field, value, columns="*"):
        self.setConection()
        cursor = self.__conn.cursor()
        cursor.execute(f"SELECT {columns} FROM {self.__table} WHERE {field} = {value}")
        return cursor.fetchall()

    def insert(self, obj):
        self.setConection()
        columns = ', '.join(obj.keys())
        values = ', '.join([f"'{value}'" if isinstance(value, str) else str(value) for value in obj.values()])
        row = self.execute(f"INSERT INTO {self.__table} ({columns}) VALUES ({values})")
        return row
    
    def update(self, obj, field, value):
        self.setConection()
        values = ', '.join([f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {value}" for key, value in obj.items()])
        row = self.execute(f"UPDATE {self.__table} SET {values} WHERE {field} = {value}")
        return f"UPDATE {self.__table} SET {values} WHERE {field} = {value}"
        
