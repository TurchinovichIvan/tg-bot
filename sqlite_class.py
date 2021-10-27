import sqlite3


class SQLite_class:

    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
        #self.row_factory = sqlite3.Row

    def get_last_folder_name(self, id_user):
        with self.connection:
            query=f"SELECT * FROM folder_name_tbl WHERE id_user= {id_user}"
            return self.cursor.execute(query).fetchall()

    def get_all_folder_name(self):
        with self.connection:
            return self.cursor.execute(f"SELECT * FROM folder_name_tbl").fetchall()
            
    def add_folder_name(self, id_user, name_folder):
        with self.connection:
            query=f"INSERT INTO folder_name_tbl (id_user,name_folder) VALUES ({id_user} , '{name_folder}')"
            return self.cursor.execute(query)

    def update_folder_name(self, id_user, name_folder):
        with self.connection:
            return self.cursor.execute(f"UPDATE folder_name_tbl SET name_folder ='{name_folder}' WHERE id_user={id_user}")
