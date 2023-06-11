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
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        query = f"INSERT INTO [User] (Name, Lastname, Email, Password) VALUES ('{name}', '{lastname}', '{email}', '{hashed_password}')"
        self.cursor.execute(query)
        self.cursor.commit()

    def check_login_user(self, email, password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.cursor.execute(
            f"SELECT Email, Password FROM [User] WHERE Email = '{email}' AND Password = '{hashed_password}'")
        data = self.cursor.fetchall()
        return data

    def check_login_admin(self, password, email="admin11@admin.com"):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.cursor.execute(
            f"SELECT Email, Password FROM [User] WHERE Email = '{email}' AND Password = '{hashed_password}'")
        data = self.cursor.fetchall()
        return data

    def display_users(self):
        self.cursor.execute("SELECT Name, Lastname, Email FROM [User] WHERE Email != 'admin11@admin.com'")
        data = self.cursor.fetchall()
        return data

    def insert_word(self, polish_word, english_word, sentence_with_gap, sentence_without_gap):
        self.cursor.execute(
            f"INSERT INTO [Word] (PolishWord, EnglishWord, SentenceWithGap, SentenceWithoutGap) VALUES ('{polish_word}', '{english_word}', '{sentence_with_gap}', '{sentence_without_gap}')")
        self.cursor.commit()

    def insert_user_progress(self, count_good_answer, email):
        user_id = self.get_user_id_from_user_progress_table(email)
        if user_id:
            self.cursor.execute(
                f"UPDATE UserProgress SET SumGoodAnswer = SumGoodAnswer + {count_good_answer}, CountSession = CountSession + 1 WHERE UserId = {user_id}")
            self.cursor.commit()
        else:
            self.cursor.execute(
                f"INSERT INTO UserProgress(UserId, SumGoodAnswer, CountSession) VALUES((SELECT Id FROM [User] WHERE Email = '{email}'), {count_good_answer}, 1)")
            self.cursor.commit()
        self.connection.commit()

    def get_user_id_from_user_progress_table(self, email):
        self.cursor.execute(f"SELECT Id FROM [UserProgress] WHERE Id = (SELECT Id FROM [User] WHERE Email = '{email}')")
        row = self.cursor.fetchone()
        if row:
            return row[0]
        return None

    def select_user_progress_data(self):
        self.cursor.execute(
            "SELECT Name, ROUND(CAST(SumGoodAnswer AS decimal) / CountSession, 1) FROM [User] U INNER JOIN UserProgress US ON U.Id = US.UserId")
        data = self.cursor.fetchall()
        return data
