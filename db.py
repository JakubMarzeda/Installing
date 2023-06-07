import pyodbc as pyodbc
import hashlib


# WZORZEC PROJEKTOWY SINGLETONA GWARANTUJACY NAM ZE TYLKO
# JEDNA INSTANCJA BAZY BEDZIE
def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class DataBase:

    # KONSTRUKTOR
    def __init__(self):
        self.connection_string = ("Driver={ODBC Driver 17 for SQL Server};"
                                  "Server=localhost;"
                                  "Database=Installing;"
                                  "Trusted_Connection=yes;")
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def select_english_word(self, id):
        self.cursor.execute(f"SELECT EnglishWord FROM Word WHERE Id = '{id}'")
        data = self.cursor.fetchall()
        return data[0][0]

    def select_polish_word(self, id):
        self.cursor.execute(f"SELECT PolishWord FROM Word WHERE Id = '{id}'")
        data = self.cursor.fetchall()
        return data[0][0]

    def select_sentence_with_gap(self, id):
        self.cursor.execute(f"SELECT SentenceWithGap FROM Word WHERE Id = '{id}'")
        data = self.cursor.fetchall()
        return data[0][0]

    def select_sentence_without_gap(self, id):
        self.cursor.execute(f"SELECT SentenceWithoutGap FROM Word WHERE Id = '{id}'")
        data = self.cursor.fetchall()
        return data[0][0]

    def insert_user_data(self, name, lastname, email, password):
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        query = f"INSERT INTO [User] (Name, Lastname, Email, Password) VALUES ('{name}', '{lastname}', '{email}', '{hashed_password}')"
        self.cursor.execute(query)
        self.cursor.commit()

    def login_user(self, email, password):
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        self.cursor.execute(
            f"SELECT Email, Password FROM [User] WHERE Email = '{email}' AND Password = '{hashed_password}'")
        data = self.cursor.fetchall()
        return data

    def check_logged_admin(self, password, email="admin11@admin.com"):
        hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        self.cursor.execute(
            f"SELECT Email, Password FROM [User] WHERE Email = '{email}' AND Password = '{hashed_password}'")
        data = self.cursor.fetchall()
        return data

    def display_users(self):
        pass

    def insert_word(self):
        pass
